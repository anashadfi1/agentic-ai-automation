
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

from ninja import Router, Schema
from ninja.errors import HttpError

router = Router()


class SignupSchema(Schema):
    username: str
    email: str
    password: str


class LoginSchema(Schema):
    username: str
    password: str


@router.get("/csrf")
@ensure_csrf_cookie
def csrf_token(request):
    return {"csrfToken": get_token(request)}


@router.post("/signup")
def signup(request, data: SignupSchema):
    username = data.username.strip()
    email = data.email.strip().lower()

    if not username or not email or not data.password:
        raise HttpError(400, "All fields are required.")

    if len(data.password) < 8:
        raise HttpError(400, "Password must be at least 8 characters.")

    if User.objects.filter(username=username).exists():
        raise HttpError(400, "Username already exists.")

    if User.objects.filter(email__iexact=email).exists():
        raise HttpError(400, "Email already exists.")

    user = User.objects.create_user(
        username=username,
        email=email,
        password=data.password,
    )

    return {
        "message": "Account created successfully.",
        "username": user.username,
    }


@router.post("/login")
def login_user(request, data: LoginSchema):
    user = authenticate(
        request,
        username=data.username,
        password=data.password,
    )

    if user is None:
        raise HttpError(401, "Invalid username or password.")

    login(request, user)

    return {
        "message": "Login successful.",
        "username": user.username,
    }


@router.post("/logout")
def logout_user(request):
    if not request.user.is_authenticated:
        raise HttpError(401, "You are not logged in.")

    logout(request)
    return {"message": "Logged out successfully."}


@router.get("/me")
def current_user(request):
    if not request.user.is_authenticated:
        raise HttpError(401, "Not authenticated.")

    return {
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
    }
