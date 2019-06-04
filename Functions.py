def target_name(name_vertex):
    return 'T_' + name_vertex


def source_name(name_vertex):
    return 'S_' + name_vertex


def source_to_target_name(name):
    list_name = list(name)
    list_name[0] = 'T'
    return ''.join(list_name)


def target_to_source_name(name):
    list_name = list(name)
    list_name[0] = 'S'
    return ''.join(list_name)


def clean_name(name):
    list_name = list(name)
    if list_name[0] == 'S' or list_name[0] == 'T':
        list_name.remove(list_name[0])

    if list_name[0] == '_':
        list_name.remove(list_name[0])

    return ''.join(list_name).lower()
