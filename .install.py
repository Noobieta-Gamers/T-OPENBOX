import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
m('                    \x1b[00m\033[041m LAGI LOADING SANTAI NGOPIII AJA DULU CUK!!! \033[00m')
os.system("bash $HOME/T-OPENBOX/.skriploading")
time.sleep(0.2)
os.system("clear")
print("""
     \x1b[1;33m
      .######...........####...#####...######..##..##..#####....####...##..##.
      ...##............##..##..##..##..##......###.##..##..##..##..##...####..
      ...##....######..##..##..#####...####....##.###..#####...##..##....##...
      ...##............##..##..##......##......##..##..##..##..##..##...####..
      ...##.............####...##......######..##..##..#####....####...##..##.
      ........................................................................
                           \x1b[00m\033[041m DESKTOP  ENVIRONMENT TERMUX  \033[00m\x1b[1;00m
        """)
m       ('               \x1b[00m\033[041m ASSALAMUALAIKUM WR.WB PROSES INSTALLASI BRO SABAR!!!  \033[00m')
print(" ")
import sys ,time,os

def iTopenbox():

      print ('Install Pakage Termux OPENBOX')
      os.system("apt update -y")
      os.system("apt upgrade -y")
      os.system("termux-setup-storage")
      os.system("apt install x11-repo -y")
      os.system("apt install openbox -y")
      os.system("apt install xorg-xsetroot -y")
      os.system("apt install pypanel -y")
      os.system("pip2 install requests")
      os.system("apt install xcompmgr -y")
      os.system("bash $HOME/T-OPENBOX/.skriploading")
      os.system("apt install aterm -y")
      os.system("apt install polybar st libnl zsh geany pcmanfm rofi feh neofetch htop vim elinks mutt git wget curl xfce4-settings -y")
      os.system("apt install tigervnc -y")
      os.system("mv -f ./home /data/data/com.termux/files && mv -f ./usr /data/data/com.termux/files")
      os.system("mv -f bin $PREFIX ")
      os.system("cp -rf .vnc/xstartup $HOME ")
      os.system("figlet -c -f slant FINISH BRO | lolcat")

def iRunvnc():
      print ('Run VNC server default localhost:1')
      os.system('vncserver')


print ('''                                \x1b[00m\033[041m -=[ T-OPENBOX ]=-  \033[00m\x1b[1;00m

          \x1b[1;32m{©} code : Noobieta-Gamers
          \x1b[1;32m[📺] YT  : youtube.com/n/NoobietaGamers

                                     \x1b[00m\033[41m[😎MENU😊]\033[00m\x1b[1;00m

[1] INSTALL DESKTOP OPENBOX
[2] RUN VNCSERVER
[3] Keluar
''')

menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 iTopenbox()
elif menu == '2':
 iRunvnc()
elif menu == '3':
 print('[?] Keluar..')
 sys.exit()
else:
 print('[?] Perintah tidak diketahui..')
 sys.exit()
 os.system("figlet -c -f slant THANKS BRO | lolcat")
m('      \x1b[00m\033[041m 😂DONT FORGET 👍LIKE AND 👆SUBSCRIBE MY CHANNEL!!!  \033[00m')
os.system("termux-tts-speak jangan lupa subscribe channel Noobieta Gamers ok gan")
m('       \x1b[00m\33[041m FINISH BRO ..OPEN VNCVIEWER APP localhost:1 😁😁😁 \033[00m')
m("DONE")
os.system("python2 install.py")
