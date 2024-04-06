import matplotlib.pyplot as plt 

fileObj = open("1kHz_44100Hz_16bit_05sec.wav", mode="rb")

data = fileObj.read()

file_size_inbytes=data[4:8]
file_size = int.from_bytes(file_size_inbytes,byteorder="little")

num_of_channels_in_byte=data[22:24]
num_of_channels = int.from_bytes(num_of_channels_in_byte,byteorder="little")

audio_data_size_inbytes=data[40:44]
audio_data_size = int.from_bytes(audio_data_size_inbytes,byteorder="little")

sample_rate_in_bute = data[24:28]
sample_rate = int.from_bytes(sample_rate_in_bute, byteorder="little")

audio_amps=[]

for i in range(0,audio_data_size,2):
    amp_in_byte=data[44+i:44+i+2]
    amp=int.from_bytes(amp_in_byte, byteorder="little", signed = True)
    audio_amps.append(amp)


plt.plot(range(len(audio_amps)),audio_amps)
plt.show()

pass