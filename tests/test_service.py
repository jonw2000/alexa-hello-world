import pytest
from src.hello_world.service import HelloWorldService

@pytest.fixture
def service():
    return HelloWorldService()

def test_welcome_message(service):
    assert service.get_welcome_message() == "Welcome to Hello World! You can say hello or help."

def test_hello_message(service):
    assert service.get_hello_message() == "Hello World!"

def test_help_message(service):
    assert service.get_help_message() == "You can say hello to me!"

def test_goodbye_message(service):
    assert service.get_goodbye_message() == "Goodbye!"

def test_personalized_message(service):
    # Test without name
    assert service.get_personalized_message() == "Hello World!"
    
    # Test with name
    assert service.get_personalized_message("Alice") == "Hello World! Nice to meet you, Alice!"