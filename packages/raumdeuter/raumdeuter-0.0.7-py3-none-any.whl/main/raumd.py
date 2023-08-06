import json
import argparse
from rich.console import Console
from rich.theme import Theme
import sys
import os
import urllib.request as urllib2
import subprocess
import platform
import socket
import signal
import ssl
from configparser import ConfigParser
from threading import Timer
from pathlib import Path
from .__init__ import __version__


# Configure the console
custom_theme = Theme({
    "good" : "green",
    "bad": "red",
    "important": "purple",
    "accent": "blue",
})

console = Console(theme=custom_theme)

# Some vars
props = Path(os.path.dirname(__file__)) / "raumd.conf"
keys = {}
separator = "="

configurer = ConfigParser()

def write_sequence_file(path):
	with open(path, "w") as f:
		empty = {}
		json.dump(empty,f)

# Read configuration
configurer.read(props)

url = configurer['working']["url"]
path = configurer['working']["path"]
_global_failearly = True if configurer['working']["failearly"] == 'Yes' or configurer['working']["failearly"] == 'Y' or configurer['working']["failearly"] == 'True' else False  
_global_verbose = True if configurer['working']["verbose"] == 'Yes' or configurer['working']["verbose"] == 'Y' or configurer['working']["verbose"] == 'True' else False  
timeout = None if (not configurer['working']["timeout"] or configurer['working']["timeout"] == '0') else int(configurer['working']["timeout"])
localssl = True if configurer['working']["localssl"] == 'Yes' or configurer['working']["localssl"] == 'Y' or configurer['working']["localssl"] == 'True' else False

if localssl:
	context = ssl._create_unverified_context()
else:
	context = None

def configure(args):
	
	if args.reset:

		url = 'https://airlocks.xyz'
		path = 'sequence.json'
		timeout = ''
		failearly = 'Yes'
		localssl = 'Yes'
		verbose = 'Yes'
				
		if not configurer.has_section('working'):
			configurer.add_section('working')

		configurer.set("working", "url", url)
		configurer.set("working", "path", path)
		configurer.set("working", "timeout", timeout)
		configurer.set("working", "failearly", failearly)
		configurer.set("working", "localssl", localssl)

	elif args.show:

		console.print("[accent]url[/accent]      :", configurer['working']["url"])
		console.print("[accent]path[/accent]     :", configurer['working']["path"])
		console.print("[accent]timeout[/accent]  :", configurer['working']["timeout"])
		console.print("[accent]localssl[/accent] :", configurer['working']['localssl'])
		console.print("[accent]verbose[/accent]  :", configurer['working']["verbose"])
		console.print("[accent]failearly[/accent]:", configurer['working']["failearly"])

	else:
		if args.url is not None:
			console.print('Setting url to: ', args.url[0])
			configurer.set("working", "url", args.url[0])
		
		if args.path is not None:
			console.print('Setting path to: ', args.path[0])
			configurer.set("working", "path", args.path[0])
		
		if args.timeout is not None:
			console.print('Setting timeout to: ', args.timeout[0])
			configurer.set("working", "timeout", str(args.timeout[0]))

		if args.failearly is not None:
			console.print('Setting failearly to: ', args.failearly[0])
			configurer.set("working", "failearly", args.failearly[0])

		if args.localssl is not None:
			console.print('Setting localssl to: ', args.localssl[0])
			configurer.set("working", "localssl", args.localssl[0])

		if args.verbose is not None:
			console.print('Setting verbose to: ', args.verbose[0])
			configurer.set("working", "verbose", args.verbose[0])

	if not args.show:
		try:
			with open(props, 'w') as configfile:
				configurer.write(configfile)
		except Exception as e: 
			console.print('An exception occurred while trying to write to the configure file.')
			console.print(e)

def run(args):

	# Get the local sequence JSON file
	try: 
		f = open (path, "r")
		default = json.load(f)
	except:
		console.print ("There is no sequence file I can find at the configured path.", style='bad')
		return

	sequence = default

	# .. Find the sequence ..
	found, run_this_sequence = find_sequence(args.id, sequence)
	
	# .. Run the sequence ..
	if not found:
		console.print ("I have nothing to run")
		return

	options = {'dryrun': False, 'failearly': args.failearly, 'verbose': args.verbose}

	with console.status("[blue]Running sequences...[/blue]\n") as status:
		try:
			run_sequence(run_this_sequence, args.params, options)
		except Exception as e:
			console.log("An error occurred while running the sequences", style="bad")
			console.log(e, style="bad")

def dryrun(args):

	# Get the local sequence JSON file
	try: 
		f = open (path, "r")
		default = json.load(f)
	except:
		console.print ("There is no sequence file I can find at the configured path.", style='bad')
		return

	sequence = default
	
	# .. Find the sequence ..
	found, run_this_sequence = find_sequence(args.id, sequence)
	
	# .. Run the sequence ..
	if not found:
		console.print ("I have nothing to run", style="bad")
		return
	
	options = {'dryrun': True, 'failearly': True}

	try:
		run_sequence(run_this_sequence, args.params, options)
	except Exception as e:
		console.log("An error occurred while running the sequences", style="bad")
		console.log(e, style="bad")

def run_sequence(sub_seq, params, options):
	if 'seq' not in sub_seq.keys() or sub_seq['seq'] is None:
		console.print ('Nothing to run', style='bads')
		return
	for entry in sub_seq['seq']:
		if "name" in entry.keys():
			console.print ('[accent]name[/accent]   :', entry["name"])
			comm = entry["command"]
			if params != None and len(params) > 0:
				for p in params:
					if separator in p:
						name, value = p.split(separator, 1)
						comm = comm.replace(name, value)

			console.print ('[accent]command[/accent]:', entry["command"])
			if not options['dryrun']:
				errcode = 0
				try:
					with subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as process:
						timer = Timer(timeout, stop_process,[process])
						timer.start()
						for line in process.stdout:
							if options["verbose"] or _global_verbose:
								console.print(line, end='', markup=False)
				finally:
					timer.cancel()

				errcode = process.returncode
				if errcode != 0:
					console.print("An error occurred while running the command!", style="bad")
					if options["failearly"] or _global_failearly:
						console.print('Fail early policy on, stopping execution.', style="bad")
						return
				else:
					console.print("Completed!", style="good")

		elif "id" in entry.keys():
			run_sequence(entry, params, options)
		else:
			console.print ("..??Booh??..")

def download(args):

	if not os.path.exists(path):
		write_sequence_file(path)

	# JSON file
	console.print("path:", path)
	f = open (path, "r")
	default = json.load(f)

	status, sequence = download_sequence(args.id)

	if status == "ok":
		console.print(sequence)
		f1 = open (path, "w")
		to = args.id[len(args.id) -1]
		if(args.rename is not None):
			to = args.rename[0]
		default[to] = sequence
		json.dump(default, f1)
	else:
		console.print('Couldn\'t find the sequence:')
		console.print(sequence)
	
def download_sequence(sequence):
    try:
        console.print(url + "/api/download/" + sequence[0])
        body = {"sub_seq": []}
        if len(sequence) > 1:
        	for entry in sequence[1:len(sequence)]:
        		body.get('sub_seq').append(entry)
        console.print (body)
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req = urllib2.Request(url + "/api/download/" + sequence[0])

        req.add_header('Content-Length', len(jsondataasbytes))
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req, jsondataasbytes, context=context)

        text = response.read()
        stud_obj = json.loads(text)

        return "ok", stud_obj
    except Exception as e:
        console.print("Oops download failed!", style="bad")
        console.print(e)
        return "nok", None

def show(args):

	# Get the local sequence JSON file
	try: 
		f = open (path, "r")
		default = json.load(f)
	except:
		console.print ("There is no sequence file I can find at the configured path.", style='bad')
		return

	sequence = default
	idz = args.id
	if (len(idz) == 0):
		one_element_seq = {'seq':[]}
		for entry in sequence:
			one_element_seq.get('seq').append({'id':entry})
		show_sequence(one_element_seq)
		return
	else:
		id = idz[0]
	found = False
	last_found_id = None
	if (id in sequence):
		last_found_id = id
		sequence = sequence[id]
		found = True
	for id_idx in range(1,len(idz)):
		id = idz[id_idx]

		for entry in sequence['seq']:
			if ("id" in entry and id == entry["id"]) or ("name" in entry and id == entry["name"]):
				last_found_id = id
				if ("id" in entry):
					sequence = entry
				else:
					one_element_seq = {'seq':[entry]}
					sequence = one_element_seq
				found = True
				break
			else:
				found = False

	if not found:
		console.print ("Last found id: ", last_found_id)
	show_sequence(sequence)

def show_sequence(sequence):
	seq = sequence.get('seq')
	for entry in seq:
		if ("name" in entry):
			console.print("[accent]name[/accent]   : " + "[good]" + entry["name"] + "[/good]")
			console.print("[accent]command[/accent]: " + "[good]" + entry["command"] + "[/good]")
		elif ("id" in entry):
			console.print("[accent]subseq[/accent]: " + "[important]" + entry["id"] + "[/important]" + 
				(" / [important]" + entry["title"] + "[/important]" if "title" in entry else ""))

def find_sequence(idz, sequence):
	id = idz[0]
	found = False
	last_found_id = None
	if (id in sequence):
		last_found_id = id
		sequence = sequence[id]
		found = True
	else:
		console.print("Couldn't find the sequence", style='bad')
		return found, None
	for id_idx in range(1,len(idz)):
		id = idz[id_idx]

		for entry in sequence['seq']:
			if ("id" in entry and id == entry["id"]) or ("name" in entry and id == entry["name"]):
				last_found_id = id
				if ("id" in entry):
					sequence = entry
				else:
					one_element_seq = {'seq':[entry]}
					sequence = one_element_seq
				found = True
				break
			else:
				found = False
	return found, sequence

def sysinfo(args):
	try:
		info={}
		console.print('platform        :',platform.system())
		console.print('platform-release:',platform.release())
		console.print('platform-version:',platform.version())
		console.print('architecture    :',platform.machine())
		console.print('platform        :',platform.platform())
		console.print('hostname        :',socket.gethostname())
	except Exception as e:
		console.print(e)

def stop_process(process):
	console.print('Timeout expired, stopping process', style='bad')
	process.terminate()

def main():
	# create parser object
	description = """Raumdeuter runs your sequence of bash commands defined in a json file. 
	This files can be created on the online platform airlocks.xyz!"""

	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers()

	run_parser = subparsers.add_parser('run', help = 'Runs a command or a sequence')
	run_parser.add_argument("id", type = str, nargs = '+', help = "The sequence or command to be executed.")
	run_parser.add_argument("--params", type = str, nargs = '*', help = "The parameters to run the sequences with.")
	run_parser.add_argument("--failearly", "-failearly", "-fe", "--fe", action='store_true', help = "If present stops on first command failure.")
	run_parser.add_argument('--verbose', '-verbose', '-v', action='store_true', help = "Print the output of commands.")
	run_parser.set_defaults(func=run)

	download_parser = subparsers.add_parser('download', help = 'Downloads a sequence from airlocks.xyz')
	download_parser.add_argument("id", type = str, nargs = '+', help = "The sequence to obtain.")
	download_parser.add_argument("--rename", type = str, nargs = '*', help = "Renames the sequence for local use.")
	download_parser.set_defaults(func=download)

	dryrun_parser = subparsers.add_parser('dryrun', help = 'Dryruns a command or a sequence')
	dryrun_parser.add_argument("id", type = str, nargs = '+', help = "The sequence or command to be executed.")
	dryrun_parser.add_argument("--params", type = str, nargs = '*', help = "The parameters to run the sequences with.")
	dryrun_parser.set_defaults(func=dryrun)
	
	show_parser = subparsers.add_parser('show', help = 'Shows the existing commands and/or a sequence')
	show_parser.add_argument("id", type = str, nargs = '*', help = "The sequence or command to be executed.")
	show_parser.set_defaults(func=show)

	configure_parser = subparsers.add_parser('configure', help = 'Configures the runner.')
	configure_parser.add_argument("--url", "-u", "-url", "--download-url", "-download-url", type = str, nargs = 1, help = "Sets the download url.")
	configure_parser.add_argument("--path", "-p", "-path", "--download-path", "-download-path", type = str, nargs = 1, help = "Path to json file holding the sequences.")
	configure_parser.add_argument("--localssl", "-localssl", type = str, nargs = 1, help = "Accept locally generated certificates. (Yes/No)")
	configure_parser.add_argument("--timeout", "-t", type = str, nargs = 1, help = "Timeout for every command in seconds.")
	configure_parser.add_argument("--failearly", "-fe", type = str, nargs = 1, help = "General exit strategy. (Yes/No)")
	configure_parser.add_argument("--reset", "-r", action='store_true', help = "Reset configuration to defaults.")
	configure_parser.add_argument("--show", "-show", action='store_true', help = "Show current configuration.")
	configure_parser.add_argument('--verbose', '-verbose', type = str, nargs = 1, help = "Print the output of commands. (Yes/No)")
	configure_parser.set_defaults(func=configure)

	sysinfo_parser = subparsers.add_parser('sysinfo', help = 'Some system info (wip).')
	sysinfo_parser.set_defaults(func=sysinfo)

	parser.add_argument("-v", "--v", "-version", "--version", action = 'version', version=__version__,
                        default = None, help = "console.prints the version of the script.")

	if len(sys.argv) <= 1:
		sys.argv.append('--help')

	args = parser.parse_known_args()

	args[0].func(args[0])

class GracefulExiter():

    def __init__(self):
        signal.signal(signal.SIGINT, self.change_state)

    def change_state(self, signum, frame):
        console.print("..Exitting..", style='bad')
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        return

flag = GracefulExiter()

if __name__ == "__main__":
    main()