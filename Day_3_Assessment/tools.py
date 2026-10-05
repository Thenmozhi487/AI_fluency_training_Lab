def get_course_fee(course):
    fees = {
        "CS101": 12000,
        "AI202": 18000,
        "DS303": 15000
    }

    return fees.get(course, "Course not found")