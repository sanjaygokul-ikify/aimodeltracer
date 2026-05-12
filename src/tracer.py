import json

def trace_model_lineage(data_sources, model_training):
    # Implement the tracing logic, creating a dictionary to store the model lineage
    model_lineage = {}
    # Iterate over the data sources and model training configuration, populating the model lineage dictionary
    for source in data_sources:
        model_lineage[source] = {}
        # Add the model training configuration to the dictionary
        model_lineage[source]['model_training'] = model_training
    return model_lineage

def save_model_lineage(model_lineage, output_file):
    # Save the model lineage to a JSON file
    with open(output_file, 'w') as f:
        json.dump(model_lineage, f, indent=4)