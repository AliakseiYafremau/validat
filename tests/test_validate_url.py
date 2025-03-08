from validat.validators.url import validate_url


def test_correct_protocol():
    """
    Check for protocols
    """
    http_url = "http://example.com"
    https_url = "https://example.com"
    incorrect_protocol_url = "incorrect://example.com"

    assert validate_url(http_url) == True
    assert validate_url(https_url) == True
    assert validate_url(incorrect_protocol_url) == False


def test_domain():
    """
    Check for domain
    """
    domain_url = "https://example.com"
    one_word_domain = "https://example"
    no_domain = "https://"
    localhost_url = "http://localhost"

    assert validate_url(domain_url) == True
    assert validate_url(one_word_domain) == False
    assert validate_url(no_domain) == False
    assert validate_url(localhost_url) == True


def test_exact_protocol():
    """
    Check for exact protocol in url
    """
    url = "https://example.com"

    correct_protocol = "https://"
    incorrect_protocol = "http://"

    assert validate_url(url, protocol=correct_protocol) == True
    assert validate_url(url, protocol=incorrect_protocol) == False


def test_exact_authority():
    """
    Check for exact authority in url
    """
    url = "https://example.com"

    correct_authority = "example.com"
    incorrect_authority = "elpmaxe.com"

    assert validate_url(url, authority=correct_authority) == True
    assert validate_url(url, authority=incorrect_authority) == False
