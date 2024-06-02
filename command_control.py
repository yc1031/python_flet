import subprocess

class CommandControl():
    def __init__(self, target):
        self.target = target
    
    def input_command(self, cmd):
        msgs = subprocess.run(cmd, encoding='utf-8', \
                                  stdout=subprocess.PIPE).stdout.splitlines()
        
        msgs = [msg.strip() for msg in msgs]

        return msgs

    def get_branches(self):
        branches = self.input_command(['git', 'branch', '-a'])
        return branches
        
    def get_commit_hash(self):
        commit_hash = self.input_command(['git', 'log', '--pretty=%H'])
        return commit_hash