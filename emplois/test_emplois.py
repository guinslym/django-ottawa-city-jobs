import pytest

@pytest.mark.django_db
def test_about_views(client):
    response = client.get('/about')
    assert response.status_code == 200

