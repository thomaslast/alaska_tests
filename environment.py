from api_wrapper import ApiWrapper


def before_all(context):
    context.api_wrapper = ApiWrapper()
    context.api_wrapper.delete_all_bears()
    context.api_wrapper.delete_a_bear(1)


def after_all(context):
    pass
    # context.api_wrapper.delete_all_bears()
    # context.api_wrapper.delete_a_bear(1)
