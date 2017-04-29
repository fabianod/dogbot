import kyoukai as kyk

WebBlueprint = kyk.Blueprint('web')


@WebBlueprint.route('/')
async def web_index(ctx: kyk.HTTPRequestContext):
    return "Hello!"
