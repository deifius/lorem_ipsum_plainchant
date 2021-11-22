#!/usr/bin/env python3

from time import sleep
from os import system
from random import random
from lorem import sentence as text
#from lorem import text
from subprocess import check_output, Popen
from sys import argv

def write_word_to_speak(word):
	with open('living_word/' + word + '.txt', 'w') as apples: 
		apples.write(word)

def speak_written_word(word):
	system('text2wave living_word/' + word + '.txt > living_word/' + word + '.wav')
	system('rm living_word/' + word + '.txt')
	#Popen(['aplay','-q','living_word/' + word + '.wav'])

def sing_spoken_word(word):
	system('echo "living_word/' + word + '.wav;"| nc localhost 6006 -q 1')
	#print('my song pid:\t' + singing_word_pid)

def loremitall(word_text, relative_speed):
	printed_text = ""
	for each_word in word_text.split(' '):
			printed_text, ok = printed_text + each_word + ' ', system('clear')
			print(printed_text + "\n\n\n\n")
			write_word_to_speak(each_word)
			speak_written_word(each_word)
			sing_spoken_word(each_word)
			sleep((len(each_word)*(random()+2))/relative_speed)
			system('rm living_word/' + each_word + '.wav')
def chanting_service():
	Popen(['pd','-nogui','-jack','word_singer.pd'])
		
def main():
	chanting_service()
	if len(argv) > 1:
		loremitall(' '.join(argv[1:]),30)
	else:
		loremitall(text(), 30)

if __name__ == "__main__": main()
