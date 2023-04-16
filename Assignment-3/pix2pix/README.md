Code used to train the model
  python train.py --dataroot ./datasets/data/ --name pix2pix_inpainting --model pix2pix --netG unet_256 --direction AtoB --lambda_L1 50 --dataset_mode aligned --norm batch --pool_size 0


Code used to test the model
Load the model from the drive into the folder checkpoints/pix2pix_inpainting and then run the following code
Link to drive: https://drive.google.com/drive/folders/1-FCK0XCVTYNGqcWMDGjPd15LNLT_6Iu-?usp=sharing
  python test.py --dataroot ./datasets/Testing_Data/ --name pix2pix_inpainting --model test --netG unet_256 --direction AtoB --dataset_mode single --norm batch

Code used to generate the results
put the masked_info.csv in the folder that contains the output images, which can be seperated from the masked images using the code in get_fake.py
After that run the code in generate_results.py after setting the appropriate path
  python generate_results.py