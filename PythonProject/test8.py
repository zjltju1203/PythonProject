import json

path = "stf_data.jsonl"

train_json = json.load(open(path, "r"))

print(train_json)

from accelerate import Accelerator, skip_first_batches, DataLoaderConfiguration


def create_accelerator_and_postprocess(self):
    grad_acc_kwargs = {"num_steps": self.args.gradient_accumulation_steps}
    grad_acc_kwargs["sync_with_dataloader"] = False
    gradient_accumulation_plugin = GradientAccumulationPlugin(**grad_acc_kwargs)

    # create accelerator object
    dataloader_config = DataLoaderConfiguration(dispatch_batches=self.args.dispatch_batches,split_batches=self.args.split_batches)
    self.accelerator = Accelerator(
        dataloader_config=dataloader_config,
        deepspeed_plugin=self.args.deepspeed_plugin,
        gradient_accumulation_plugin=gradient_accumulation_plugin,
    )
