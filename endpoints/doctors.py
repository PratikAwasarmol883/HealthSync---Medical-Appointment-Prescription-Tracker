from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.doctors import Doctors
from models.request_body import CreateDoctorsProfileRequestBody, UpdateDoctorsProfileRequestBody

router = APIRouter(tags=["Doctors Info"])

@router.post(
        path= "",
        summary= "Create Doctors Profile."
)
async def create_doctor_profile(
    doctors: CreateDoctorsProfileRequestBody
):
    try:
        doctor_obj = Doctors(
            name = doctors.name,
            phone_number = doctors.phone_number,
            email = doctors.email,
            hospital = doctors.hospital,
            city = doctors.city,
            highest_degree = doctors.highest_degree,
            speciality = doctors.speciality,
            years_of_experience = doctors.years_of_experience,
            registration_number = doctors.registration_number
        )
        res = await doctor_obj.create()
        response_data = jsonable_encoder(res)
        return JSONResponse(
            content={
                "message": "Doctor Profile created successfully.",
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
        path= "",
        summary= "Get all doctors details."
)
async def get_doctors_details(
    skip: int=0, limit: int=10
):
    try:
        doctors = await Doctors.find_all().skip(skip).limit(limit).to_list()
        total_count = await Doctors.count()

        return {
            "pagination":{
            "total":total_count,
            "skip":skip,
            "limit":limit,
            "page": (skip // limit) + 1,
            "pages": (total_count + limit - 1) // limit
        },
        "data" : doctors
        }
    except Exception as ex:
        print(ex)


@router.get(
        path="/{doctors_id}",
        summary="Get doctors profile by id."
)
async def get_doctors_profile_by_id(doctors_id):
    doctor_details = await Doctors.get(doctors_id)
    return doctor_details


@router.put(
        path="/{doctor_id}",
        summary="Update doctors profile."
)
async def update_doctor_profile(
    doctor_id,
    doctor : UpdateDoctorsProfileRequestBody= Body(..., description="Update user details.")):
    try:
        doctor_details = await Doctors.get(doctor_id)
        if not doctor_details:
            return JSONResponse(
                content={"message": "User not found"},
                status_code=404
            )
        update_data = doctor.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(doctor_details,field,value)

        await doctor_details.save()

        return JSONResponse(
            content={
                "message": "User updated successfully",
                "data": jsonable_encoder(doctor_details)
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
    path= "/{doctor_id}",
    summary="Delete doctors profile."
)
async def delete_doctor_profile(doctor_id):
    try:
        doctor = await Doctors.get(doctor_id)
        if doctor:
            await doctor.delete()
            return JSONResponse(
                content={"message": "User Profile deleted Succefully."},
                status_code= 200
            )
        else:
            return JSONResponse(
                content={"message": "User Not Found."},
                status_code= 401
            )
    except Exception as ex:
        print(ex)