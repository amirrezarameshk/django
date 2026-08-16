datas = [
    {"name": "ali", "score": 4, "reason": "alpha"},
    {"name": "ahamd", "score": 2, "reason": "beta"},
    {"name": "reza", "score": 1, "reason": "delta"},
]

datas.append({"name": "amirreza", "score": 5, "reason": "gamma"})
datas.append({"name": "mohammad", "score": 3, "reason": "epsilon"})

def get_mood_status(score: int):
    if score == 5:
        status = "excellent"
    elif score == 4:
        status = "good"
    elif score == 3:
        status = "normal"
    else: 
        status = "needs attention"
    return status

needs_attention_count = 0
sum_score = 0
people_count = 0

for data in datas:
    user_status = get_mood_status(data["score"])
    data["status"] = user_status
    print(data["name"], user_status, data)
    
    sum_score += data["score"]
    people_count += 1
    
    if user_status == "needs attention":
        needs_attention_count += 1


average_mood = sum_score / people_count


print(f"all people: {people_count}") 
print(f"average mood: {average_mood}") 
print(f"number of needs attention: {needs_attention_count}")

if average_mood >= 4:
    overall_status = "excellent"
elif average_mood >= 3:
    overall_status = "good"
elif average_mood >= 2:
    overall_status = "normal"
else:
    overall_status = """iran 
     / \\
    / ! \\
   /_____\\ """

print(f"final status : {overall_status}")