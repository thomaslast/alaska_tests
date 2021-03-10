from api_wrapper import ApiWrapper


def before_all(context):
    context.api_wrapper = ApiWrapper()
    context.delete_all_bears()


def after_all(context):
    pass
    #context.delete_all_bears()
