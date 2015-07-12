import profile
import random

def generate_random_array(array_size):
	return random.sample(range(1,100), array_size)
	
	

def hello_world():
	print("Hello World")

def main():
	profile.run('hello_world')

if __name__=='__main__':
    main()

x = generate_random_array(5)

print x
