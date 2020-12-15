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

        # For the 'components' value ONLY
        elif key == 'components':
            c_string = f"**{cap_key}:** " + ', '.join([str(c) for c in value])
            # Replace the one-letter abbreviations with long form.
            out_string = c_string.replace("V", "Verbal").replace("S", "Somatic").replace("M", "Material")
            output_list.append(out_string)

    output = '\n'.join([str(i) for i in output_list])
    return output


def list_damage(data):
    name = '**Name:** ' + data['name']
    output_list = [name]

    for key, value in data['damage'].items():
        # cap_key = key.replace('_', ' ').capitalize()
        if key == 'damage_type':
            out_string = f"**Damage Type:** {value['name']}"
            output_list.append(out_string)
        if key == 'damage_at_slot_level':
            for level, dice in value:
                # TODO: add functionality to add dice per level to embed

    output = '\n'.join([str(i) for i in output_list])
    return output
