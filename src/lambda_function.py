from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from hello_world.service import HelloWorldService

# Initialize service
service = HelloWorldService()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "LaunchRequest"

    def handle(self, handler_input):
        speak_output = service.get_welcome_message()
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelloWorldIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "IntentRequest" and \
               handler_input.request_envelope.request.intent.name == "HelloWorldIntent"

    def handle(self, handler_input):
        # Example of getting slot value if needed
        # slots = handler_input.request_envelope.request.intent.slots
        # name = slots['name'].value if 'name' in slots else None
        # speak_output = service.get_personalized_message(name)
        
        speak_output = service.get_hello_message()
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "IntentRequest" and \
               handler_input.request_envelope.request.intent.name == "AMAZON.HelpIntent"

    def handle(self, handler_input):
        speak_output = service.get_help_message()
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (handler_input.request_envelope.request.object_type == "IntentRequest" and
                (handler_input.request_envelope.request.intent.name == "AMAZON.CancelIntent" or
                 handler_input.request_envelope.request.intent.name == "AMAZON.StopIntent"))

    def handle(self, handler_input):
        speak_output = service.get_goodbye_message()
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())

def lambda_handler(event, context):
    return sb.lambda_handler()(event, context)