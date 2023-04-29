from sgplib import Package
data="你好，世界！鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美".encode("utf-8")
before=data
print(f"Raw: {data.decode('utf-8')}")
print(f"Sizeof raw data: {data.__sizeof__()} bytes")
zipper=Package()
data=zipper.encode(data,zip_level=9)
print(f"Is zipped: {zipper.zipped}")
print(f"Final data size: {data.__sizeof__()}")
print("Decode...")
zipper=Package()
data=zipper.decode(data)
print(f"Got raw: size {data.__sizeof__()}")
print(data.decode("utf-8"))
print(f"Compare...")
if before == data:
    print("SAME!")
else:
    print("Fail...")