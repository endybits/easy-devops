from app.main import hello_devops, home


def test_returns_dict():
    """
    Tests that the function returns a dictionary
    """
    response = home()
    assert isinstance(response, dict)




def test_valid_name():
    """
    Tests that the function returns a greeting message 
    with a valid name parameter.
    """
    response = hello_devops('John')
    assert response['greeting'] == 'Hello John'
    assert response['mesagge'] == "I'm a microservice developed with the best practices of DevOps"
    assert response['author'] == 'Endy Bermudez'
    assert response['cta'] == 'Follow me on https://www.linkedin.com/in/endyb/'


def test_numbers_name():
    """
    Tests that the function returns a greeting message 
    with a name parameter containing numbers
    """
    response = hello_devops('John123')
    assert response['greeting'] == 'Hello John123'
    assert response['mesagge'] == "I'm a microservice developed with the best practices of DevOps"
    assert response['author'] == 'Endy Bermudez'
    assert response['cta'] == 'Follow me on https://www.linkedin.com/in/endyb/'
