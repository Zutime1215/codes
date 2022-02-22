import requests
import json

from collections import defaultdict

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=SJjqzxv2ZT07f-fa-LHqJpeoIZsQrX_CPN3eFPHTGcEAJbdG7PPRw4T00B5cany4nae4MK2P4x0sCM-ABGcX2QQRmSmJcbLXm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIeJHNDtjqcnA2i8f9f8mDF7sG1NILZMwucRrYzx2Nv-Nc4Cxuv7_z6E0oDJsLMRmcz6WQMcZSGpRJAqDnmp-YkhzNwIKjdCG2f9hfdWLiBtf_vOLj7QN4c&lib=MuYY0LBp_KVm_skCz-w6cptm_AyeNRI0M'

html_text = requests.get(url).text
data = json.loads(html_text)
# print(type(data))
routines = data['routines']

# version defaultdict
#same_subjects = defaultdict(list)
#for routine in routines:
#	same_subjects[routine['subject'].lower()].append(routine)

#version dict
same_subjects = {}
for routine in routines:
	key = routine['chapter'].lower()
	routine_list = same_subjects.get(key)
	
	if not routine_list:
		same_subjects[key] = [routine]
	else:
		routine_list.append(routine)


print(len(routines), same_subjects['ভেক্টর - ০১'])

# purify_info = json.dumps(data, indent=2, sort_keys=True) + '\n\n'
