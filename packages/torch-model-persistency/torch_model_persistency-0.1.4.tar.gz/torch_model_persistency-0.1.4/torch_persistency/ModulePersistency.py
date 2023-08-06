import torch
import os
from shutil import rmtree

class ModulePersistency:

    def __init__(self,checkpoint_dir,version = None):

        if not version:
            try:
                with open("torch_persistency.env","r+") as fp:

                    version = int(fp.read())
                    # Delete all content in file.
                    
            except FileNotFoundError:
                version = 0
            
            except ValueError:
                version = 0
                
            
            finally:
                with open("torch_persistency.env","w") as fp:
                    fp.write(f"{version+1}")

        self.checkpoint_dir = checkpoint_dir
        self.version = version
        self.save_dir = os.path.join(self.checkpoint_dir,str(self.version))
        self._prepare()


    def best(self,module,name=None):
        self._save(module,"best",name)


    def _save(self,module,tag,name):
        if not name:
            name = type(module).__name__

        torch.save(module,os.path.join(self.save_dir,f"{name}_{tag}.pt"))

    def _prepare(self):
        pathlib.Path(self.save_dir).mkdir(parents=True, exist_ok=True)


    def save(self,module,epoch : int,name = None):
        self._save(module,epoch,name)
        

