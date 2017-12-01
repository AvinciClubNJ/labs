def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    return build_response("Welcome! This is Avinci Club. Enjoy programming.")


def build_response(message):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': "Welcome! This is Avinci club. Enjoy programming!"
            },
            'shouldEndSession': True            
        }
    }
