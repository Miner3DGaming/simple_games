def _parse_msy(data:str)->dict:
    # Miner3D's Simplified YAML
    parsed_data = {}
    current_list_name = None
    
    lines = data.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            current_list_name = line[1:].strip()
            parsed_data[current_list_name] = []
        elif line:
            if current_list_name is not None:
                parsed_data[current_list_name].append(line)
            else:
                raise ValueError("Data format error: Item found before list name.")
    
    return parsed_data

def _format_msy(data:dict)->str:
    formatted_text = ""
    
    for list_name, items in data.items():
        formatted_text += f"#{list_name}\n"
        for item in items:
            formatted_text += f"{item}\n"
        formatted_text += "\n"
    
    return formatted_text

def load(text:str)->dict:
    """
        Returns a dictionary based on the inputted string (msy format)
    """
    return _parse_msy(data=text)
    
def format(text:str)->str:
    """
        Returns a a str (msy formatted) from the inputted dictionary
    """
    return _format_msy(data=text)