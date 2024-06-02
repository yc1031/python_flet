import subprocess

class CommandControl():
    def __init__(self, target):
        self.target = target
    
    def input_command_and_get_stdout(self, cmd):
        msgs = subprocess.run(cmd, encoding='utf-8', \
                                  stdout=subprocess.PIPE).stdout.splitlines()
        
        msgs = [msg.strip() for msg in msgs]

        return msgs
    
    def input_command(self, cmd):
        subprocess.run(cmd)
        

    def get_branches(self):
        branches = self.input_command_and_get_stdout(['git', 'branch', '-a'])
        return branches
        
    def get_commit_hash(self):
        commit_hash = self.input_command_and_get_stdout(['git', 'log', '--pretty=%H'])
        return commit_hash
    
    def exec_pull(self):
        self.input_command(['git', 'pull'])

    def exec_checkout(self, target):
        self.input_command(['git', 'checkout', target])