from torchvision.datasets.vision import VisionDataset
from torch.utils.data import Dataset
from PIL import Image
import os
import os.path
from typing import Any, Callable, Optional, Tuple, List
import copy
import src.presets
import os.path as osp
import glob 

class COCODatasets(VisionDataset):
    def __init__(
        self,
        root: str,
        annFile: str,
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        transforms: Optional[Callable] = None,
    ):
        super().__init__(root, transforms, transform, target_transform)
        from pycocotools.coco import COCO

        self.coco = COCO(annFile)
        self.ids = list(sorted(self.coco.imgs.keys()))

    def _load_image(self, id: int) -> Image.Image:
        path = self.coco.loadImgs(id)[0]["file_name"]
        return Image.open(os.path.join(self.root, path)).convert("RGB"), path.split('/')[-1].split('.')[0]

    def _load_target(self, id) -> List[Any]:
        return self.coco.loadAnns(self.coco.getAnnIds(id))

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        id = self.ids[index]
        image, fname = self._load_image(id)

        target = self._load_target(id)

        if self.transforms is not None:
            image, target = self.transforms(image, target)

        return image, target, fname

    def __len__(self) -> int:
        return len(self.ids)


class MASKDatasets(Dataset):
    def __init__(self, root_dir, mode, transforms=None):
        self.root_dir = root_dir
        self.transforms = transforms
        self.mode = mode 
        self.img_files = glob.glob(os.path.join(self.root_dir, mode, "images", "*.jpg"))
    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx): 
        img_file = self.img_files[idx]
        fname = osp.split(osp.splitext(img_file)[0])[-1]

        mask_file = osp.join(self.root_dir, self.mode, 'masks/{}.png'.format(fname))
        if not osp.exists(mask_file):
            raise Exception(f"There is no such mask image {mask_file}")

        image = Image.open(self.img_files[idx])
        mask = Image.open(mask_file)        
        
        if self.transforms is not None:
            image, target = self.transforms(image, mask)

        return image, target, fname


