#This is a python calculator used to calculate tick and cm for the auton period of the ftc

def main():
    default_ticks_per_rotation=4
    one_rot_ticks = 0
    final_ticks = 0
    agbox = []
    print(" Cᴏᴘʏʀɪɢʜᴛ © Gᴠᴏʟ & Gᴇᴏʀɢᴇᴍᴇᴄʜ 2023 ᴅᴏ ɴᴏᴛ ʀᴇsᴇʟʟ ")
    print("█▀▄ █▀█   █▄█ █▀█ █░█   ▄▀█ █▀▀ █▀▀ █▀ █▀▀ █▀█ ▀█▀   █▄█ ░░▄▀ █▄░█")
    print("█▄▀ █▄█   ░█░ █▄█ █▄█   █▀█ █▄▄ █▄▄ ▄█ ██▄ █▀▀ ░█░   ░█░ ▄▀░░ █░▀█")
    agnolage = input(">>>")
    if agnolage == "y" or agnolage == '"y"':
        has_g_box=input("does your motor have gear boxes? y/n\n")
        w_rad=int(input("Add your wheel's perimeter (perimetro) in CM \n"))
        target_dest=int(input("Add the target distance you want to go in CM\n"))
        if has_g_box == "y":
            threeto1check=input("Do you have a 3:1 gearbox on the motor? y/n\n")
            fourto1check=input("Do you have a 4:1 gearbox on the motor? y/n\n")
            fiveto1check=input("Do you have a 5:1 gearbox on the motor? y/n\n")
            if threeto1check == "y":
                agbox.append(3)
            if fourto1check== "y":
                agbox.append(4)
            if fiveto1check == "y":
                agbox.append(5)
            one_rot_ticks = default_ticks_per_rotation
            for i in agbox:
                one_rot_ticks = one_rot_ticks * i

            rot_needed = target_dest / w_rad
            final_ticks = one_rot_ticks * rot_needed
            rounded_ticks = round(final_ticks, 2)
            print(10*"\n")
            print("The ticks you need to put on your code are" +" " + str(rounded_ticks))
            print("\n")
            print("Notice: This program runs in a loop")
            return
        if has_g_box == "n":
            rot_needed = target_dest / w_rad
            final_ticks = rot_needed * default_ticks_per_rotation
            rounded_ticks = round(final_ticks, 2)
            print(10*"\n")
            print("The ticks you need to put on your code are" +" " + str(rounded_ticks))
            print("\n")
            print("Notice: This program runs in a loop")
            return
        

    else:
        print(10*"\n")
        print('if you belive this is an error try typing "y"')
        print("\n")
        print("Notice: This program runs in a loop")
        return
while 1 ==1:        
    main()