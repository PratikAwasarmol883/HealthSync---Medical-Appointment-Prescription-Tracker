from fastapi import APIRouter as UserRouter
from fastapi import Request, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder  # ✅ important
from models import request_body
from models.users import Users

router = UserRouter(tags=["user"])

@router.post(
    path = "",
    summary = "Create user"
)
async def create_user(
    user: request_body.CreateUserRequestBody = Body(..., description="Create a new user.")
):
    try:
    
        user_obj = Users(**user.dict())
        res = await user_obj.create()

        response_data = jsonable_encoder(res)

        return JSONResponse(
            content={
                "message": "User created successfully.",
                "data": response_data
            },
            status_code=201
        )
    except Exception as e:
        print(f"Failed to create user: {e}")
        return JSONResponse(
            content={"message": "Internal Server Error"},
            status_code=500
        )
    

@router.get(
    path = "",
    summary = "Get users"
)
async def get_users(
    skip: int=0, limit: int=10
):
    users = await Users.find_all().skip(skip).limit(limit).to_list()
    total_count = await Users.count()

    return {
        "pagination":{
            "total":total_count,
            "skip":skip,
            "limit":limit,
            "page": (skip // limit) + 1,
            "pages": (total_count + limit - 1) // limit
        },
        "data" : users
    }


@router.get(
    path = "/{user_id}",
    summary = "Get user by user id."
)
async def get_user_by_id(user_id):
    user = await Users.get(user_id)
    if user:
        return JSONResponse(
            content={"data": jsonable_encoder(user)},
            status_code=200
        ) 
    return JSONResponse(
        content={"message": "User not found"},
        status_code=404
    )

@router.put(
    path="/{user_id}",
    summary="Update user by id.",
)
async def update_user_by_id(
    user_id: str, 
    user: request_body.UpdateUserRequestBody = Body(..., description="Update user details.")
):
    try:

        user_details = await Users.get(user_id)
        if not user_details:
            return JSONResponse(
                content={"message": "User not found"},
                status_code=404
            )

        update_data = user.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(user_details, field, value)

        await user_details.save()

        return JSONResponse(
            content={
                "message": "User updated successfully",
                "data": jsonable_encoder(user_details)
            },
            status_code=200
        )

    except Exception as ex:
        print(f"Exception: {ex}")
        return JSONResponse(
            content={"message": "Internal server error"},
            status_code=500
        )
  

@router.delete(
    path="/{user_id}",
    summary="Delete user by id."
)
async def delete_user_by_id(user_id):
    user = await Users.get(user_id)
    if user:
        await user.delete()
    else:
        return "User Does not exist with that particular id."



# Renaming the router.
UserRouter = router
