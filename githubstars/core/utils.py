def remove_tag_duplicate(tags):
    """ remove tag duplicated """
    final_tags = ''
    tags_split = tags.split(',')
    tags = list(set(tags_split))
    for i, tag in enumerate(tags):
        if i == 0:
            final_tags += tag
        else:
            final_tags += ',%s' % tag

    return final_tags
