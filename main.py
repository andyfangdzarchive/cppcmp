import sys
import filecmp
import os

def compile(filename):
  prefix, suffix = filename.split('.')
  if suffix == "py":
    return ['python', filename]
  elif suffix == "cpp":
    call(['g++', filename])
    return ['./a.out']

def redirect(command, input_f=None, output_f=None):
  if input_f is not None:
    command += ['<', input_f]
  if output_f is not None:
    command += ['>', output_f]
  return command

def call(command):
  os.system(" ".join(command))

if __name__ == "__main__":
  GENERATOR = sys.argv[1]
  PRGM1 = sys.argv[2]
  PRGM2 = sys.argv[3]
  INPUT_FILE = "input.txt"
  N = int(sys.argv[4])
  generator_cmd, prgm1_cmd, prgm2_cmd = [ compile(x) for x in [GENERATOR, PRGM1, PRGM2] ]

  correct = 0
  for i in range(N):
    call(redirect(generator_cmd, output_f=INPUT_FILE))
    call(redirect(prgm1_cmd, input_f=INPUT_FILE, output_f="prgm1.out"))
    call(redirect(prgm2_cmd, input_f=INPUT_FILE, output_f="prgm2.out"))
    if filecmp.cmp("prgm1.out", "prgm2.out"):
      print("Execution %d correct." % (i + 1))
      correct += 1
    else:
      print("Execution %d error." % (i + 1))

  print("Test completed. AC rate:%d/%d" % (correct, N))
