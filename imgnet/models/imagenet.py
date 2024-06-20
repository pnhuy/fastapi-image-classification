from PIL import Image
import torch
from torchvision import transforms
import urllib.request

from logging import getLogger

logger = getLogger()


class ResNetPipeline:
    def __init__(self):
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
        self.model.eval()
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        self.classes = self._get_class_names()

    def _get_class_names(self):
        target_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
        lines = urllib.request.urlopen(target_url).readlines()
        categories = [str(s.decode('utf8')).strip() for s in lines]
        return categories

    def predict(self, filename: str):
        input_image = Image.open(filename)
        input_tensor = self.preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)

        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            self.model.to('cuda')

        with torch.no_grad():
            output = self.model(input_batch)

        probs = torch.nn.functional.softmax(output)

        top5_prob, top5_catid = torch.topk(probs, 5)

        output = []
        for p, c in zip(top5_prob[0], top5_catid[0]):
            output.append(
                dict(
                    name=self.classes[int(c.item())],
                    prob=p.item()
                )
            )

        return output
        

