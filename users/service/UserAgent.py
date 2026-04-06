from user_agents import parse

def parse_user_agent(user_agent_string: str):
    if not user_agent_string:
        return None

    ua = parse(user_agent_string)

    browser = f"{ua.browser.family} {ua.browser.version_string}"
    os = f"{ua.os.family} {ua.os.version_string}"

    return f"{os} | {browser}"


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def get_device(user_agent_string):
    if not user_agent_string:
        return None

    ua = parse(user_agent_string)
    return f"{ua.os.family} | {ua.browser.family}"