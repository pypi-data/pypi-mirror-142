import json

def main():
	with open('5.json') as json_file:
		data = json.load(json_file)
		print(data)

if __name__ == "__main__":
    main()
