import torch
import os
from shutil import rmtree
import pathlib
from glob import glob


class ModulePersistency:

    def __init__(self,checkpoint_dir = "checkpoint",version = None):

        if version is None:
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


    def best(self,module):
        self._save(module,"best")


    def _save(self,module,tag):
        
        torch.save(module.state_dict(),os.path.join(self.save_dir,f"checkpoint_{tag}.pt"))

    def _prepare(self):
        pathlib.Path(self.save_dir).mkdir(parents=True, exist_ok=True)


    def save(self,module,epoch : int):
        self._save(module,epoch)
        

    def load(self):
        

        if len(os.listdir(self.save_dir)) == 0:
            return None

        best_path = os.path.join(self.save_dir,f"checkpoint_best.pt")

        if os.path.exists(best_path):
            return torch.load(best_path)
        else:
            list_of_files = glob(self.save_dir) # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            return torch.load(latest_file)
