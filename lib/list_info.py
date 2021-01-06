def delete_info(data):
    del data['index']
    del data['url']


def list_all(data):
    output_list = []
    for key, value in data.items():
        # Capitalize first letter in every key to make the output more presentable.
        cap_key = key.replace('_', ' ').capitalize()

        # If the value of the key isn't a list or a dictionary, straight up print it
        if not isinstance(value, list) and not isinstance(value, dict):
            out_string = f"**{cap_key}:** {value}"
            output_list.append(out_string)

        # If the value is a list but only consists of one thing, print it
        elif isinstance(value, list) and len(value) == 1 and isinstance(value[0], str):
            out_string = f"**{cap_key}:** {value[0]}"
            output_list.append(out_string)

        elif key == 'desc' and len(value) > 1:
            desc = f"**{cap_key}:** " + '\n'.join([str(i) for i in value])
            output_list.append(desc)

        # For the 'components' value ONLY
        elif key == 'components':
            c_string = f"**{cap_key}:** " + ', '.join([str(c) for c in value])
            # Replace the one-letter abbreviations with long form.
            out_string = c_string.replace("V", "Verbal").replace("S", "Somatic").replace("M", "Material")
            output_list.append(out_string)

    output = '\n'.join([str(i) for i in output_list])
    return output


def list_damage_type(data):
    output_list = []
    name = '**Name:** ' + data["name"]
    desc = '**Description:** ' + data["desc"][0]
    damage_type = '**Damage Type:** ' + data["damage"]["damage_type"]["name"]
    output_list.append(name)
    output_list.append(desc)
    output_list.append(damage_type)

    output = '\n'.join([str(i) for i in output_list])
    return output