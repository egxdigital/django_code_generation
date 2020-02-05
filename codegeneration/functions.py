import csv
from codegeneration.models import *
from codegeneration.helpers import *

django_model_objects = {}
foreignkeynames_models = {}

def generate_models(inp, djangoapp):

    with open(inp) as fd:
        rdr = csv.reader(fd, delimiter=',')
        next(rdr)

        for row in rdr:
            djangofield = row[0]
            fieldname = row[1]

            if djangofield == 'models.Model':
                model_name = fieldname

                # Save some data
                underscored = helper_return_underscore_separated_fieldname(model_name)
                foreignkeynames_models[underscored] = model_name

                # Create object and save
                obj = DjangoModel(model_name, djangoapp)
                obj.add_line_to_models_code_fragment(djangofield, fieldname)
                obj.add_line_to_test_models_code_fragment(djangofield, fieldname)
                django_model_objects[model_name] = obj


            list_of_models = foreignkeynames_models.values()

            if fieldname in list_of_models:
                curr = django_model_objects.get(fieldname)

            if djangofield == 'ForeignKey':
                fkey_model_name = foreignkeynames_models.get(fieldname)
                foreignkeymodel = django_model_objects.get(fkey_model_name)
                curr.add_foreign_keys(foreignkeymodel)

            if fieldname not in list_of_models:
                curr.add_field(djangofield, fieldname)


def generate_code(*djangoapps_inputfiles:tuple):
    """Takes an arbitary number of tuples of the form ('appname', 'input file')
    and generates appname_models.py and appname_test_models.py

    Parameters
    ----------
    *djangoapps_inputfiles : tuple
        Description of parameter `*djangoapps_inputfiles`.

    Returns
    -------
    type
        Description of returned object.

    """

    filepaths = {}
    appnames = []

    for tup in djangoapps_inputfiles:
        appname = tup[0]
        input_csv = tup[1]
        filepaths[appname] = helper_return_dest_models_py_filepath(appname)
        appnames.append(appname)
        generate_models(input_csv, appname)

    for appname in appnames:
        dest_models = filepaths[appname][0]
        dest_test_models = filepaths[appname][1]
        helper_prepare_models_py(dest_models)

    for model in django_model_objects.keys():
        m = django_model_objects.get(model)

        for appname in appnames:
            if m.djangoapp == appname:
                dest_models = filepaths[appname][0]
                dest_test_models = filepaths[appname][1]

                with open(dest_models, 'a') as modelspy:
                    modelspy.write(m.models_code_fragment)

                with open(dest_test_models, 'a') as testpy:
                    testpy.write(m.test_models_code_fragment)

    for appname in appnames:
        models = {}
        for model in django_model_objects.values():
            if model.djangoapp == appname:
                models[helper_return_underscore_separated_fieldname(model.modelname)] = model.modelname
        helper_prepare_test_models_py(appname, models, filepaths[appname][1])


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'data'))

    src1 = '{}/jobsdatastore.csv'.format(data_dir)
    src2 = '{}/jobsdatabucket.csv'.format(data_dir)

    jobsdatastore = ('jobsdatastore', src1)
    jobsdatabucket = ('jobsdatabucket', src2)

    generate_code(jobsdatastore,jobsdatabucket)
