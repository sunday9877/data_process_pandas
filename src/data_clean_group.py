def clean_1(penguins):
    """
    pandas data cleaning function
    take dataframe penguins
    select 'Species','Island','Sex','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)', 'Body Mass 
    make column lower case and replace with '_', drop mm gg
    split the first word of column and make it lower case
    """
    
    ###pick up interested column
    focus = ['Species','Island','Sex','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)', 'Body Mass (g)']
    simplified = penguins[focus]

    edited_columns = ['species','island','sex','culmen_length', 'culmen_depth','flipper_length','body_mass']
    simplified.columns = edited_columns


    species = simplified['species'].unique()
    simple_species_dict={x:x.split(' ')[0].lower() for x in species}


    simplified = simplified.assign(species = lambda x: x['species'].map(simple_species_dict))

    simplified  = simplified.assign(island = lambda x: x.island.str.lower())
    simplified = simplified.assign(sex = lambda x: x['sex'].str.lower())
    simplified = simplified.dropna(axis=0)
    
    return simplified

def mean_by_sex_species(penguins):
    simplified = clean_1(penguins)
    numerical_variables = ['culmen_length','culmen_depth','flipper_length','body_mass']
    mean_by_sex_and_species = (
        simplified[["sex", "species"] + numerical_variables]
        .groupby(["sex", "species"])
        .mean())
    return mean_by_sex_and_species
