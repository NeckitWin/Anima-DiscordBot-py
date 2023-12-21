import disnake
from disnake.ext import commands

class Duel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'Bot Loaded | Duel.py ✅')
  
  @commands.slash_command(name="duel", description="Выберите, кого вызвать на дуэль из участников сервера")
  async def duel(self, ctx, user: disnake.User):
    embed1 = disnake.Embed(title="Вызов на дуэль!",description=f"Готовы ли вы принять участие в битве ВЕКА?\nЕсли вы откажитесь, то потеряете очко и честь!",color=0x00ff00)
    embed1.set_thumbnail(url=user.display_avatar.url)

    if ctx.author.id == user.id:
      await ctx.send(f"{user.display_name}, нельзя вызывать самого себя!")
      return

    self.changePos = True
    self.firstUserCounter = 0
    self.secondUserCounter = 0
    self.attackChoose = 0
    self.defChoose = 0
    self.win = False
  
    async def buttonUserWin(interaction: disnake.Interaction):
      new_embed = disnake.Embed(title=f"{interaction.user.display_name}, победил в дуэли!", description=f"Он победил со счётом:  \n1) {ctx.author.display_name} - {self.firstUserCounter}! \n2) {user.display_name} - {self.secondUserCounter}!", color=0xffd700)
      new_embed.set_thumbnail(url=interaction.author.display_avatar.url)
      await interaction.response.edit_message(embed=new_embed, view=None)

    async def checkWin():

      if self.attackChoose == self.defChoose and self.defChoose > 0:
        if self.checkUser == ctx.author.id:
          self.firstUserCounter = self.firstUserCounter + 1
        elif self.checkUser == user.id:
          self.secondUserCounter = self.secondUserCounter + 1

      if (self.firstUserCounter == 3):
        self.win = True
      if (self.secondUserCounter == 3):
        self.win = True

    async def button_callback(interaction: disnake.Interaction, button_type: str):
      self.interactionCheck = interaction.user.id

      if button_type == 'soft':
          self.attackChoose = 1
          await buttonDefend(interaction)
          return
        
      elif button_type == 'hard':
          self.attackChoose = 2
          await buttonDefend(interaction)
          return
        
      elif button_type == 'dodge':
          self.defChoose = 2
          if self.interactionCheck == self.checkUser:
            await checkWin()
          if self.win == True:
            await buttonUserWin(interaction)
          else:
            await buttonFist(interaction)
          return
        
      elif button_type == 'block':
          self.defChoose = 1
          if self.interactionCheck == self.checkUser:
            await checkWin()
          if self.win == True:
            await buttonUserWin(interaction)
          else:
            await buttonFist(interaction)
          return

    async def buttonFist(interaction: disnake.Interaction): 
      if self.contCheck:   
        if interaction.user.id != self.checkUser:
          # await interaction.send(f"{interaction.user.name}, ход другого игрока!")
          return buttonFist
      else:
        self.contCheck = True  

      if (self.changePos): 
        self.checkUser = ctx.author.id
        self.nameUser = ctx.author.display_name
        self.avatarUser = ctx.author.display_avatar.url
      else:
        self.checkUser = user.id
        self.nameUser = user.display_name
        self.avatarUser = user.display_avatar.url
          
      soft_button = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Мягкий кулак", custom_id="buttonSoft")
      hard_button = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Твёрдый кулак", custom_id="buttonHard")

      view1 = disnake.ui.View()
      view1.add_item(soft_button)
      view1.add_item(hard_button)
          
      new_embed = disnake.Embed(title=f"Ходит игрок, {self.nameUser}!", description=f"Выбери кулак которым будешь бить!\nСчёт: \n1) {ctx.author.display_name} - {self.firstUserCounter}!\n2) {user.display_name} - {self.secondUserCounter}!", color=0xffd700)
      new_embed.set_thumbnail(url=self.avatarUser)
      
      soft_button.callback = lambda i: button_callback(i,'soft')
      hard_button.callback = lambda i: button_callback(i,'hard')

      self.changePos = not self.changePos
      await interaction.response.edit_message(embed=new_embed, view=view1)
    
    async def buttonDefend(interaction: disnake.Interaction):
      if interaction.user.id != self.checkUser:
        # await interaction.send(f"{interaction.user.name}, ход другого игрока!")
        return buttonDefend
      
      if (self.changePos): 
        self.checkUser = ctx.author.id
        self.nameUser = ctx.author.display_name
        self.avatarUser = ctx.author.display_avatar.url
      else:
        self.checkUser = user.id
        self.nameUser = user.display_name
        self.avatarUser = user.display_avatar.url
      
      new_embed = disnake.Embed(title=f"Ходит игрок, {self.nameUser}!", description=f"Выбери спобос которым будешь защищаться!\nСчёт: \n1) {ctx.author.display_name} - {self.firstUserCounter}!\n2) {user.display_name} - {self.secondUserCounter}!", color=0xffd700)
      new_embed.set_thumbnail(url=self.avatarUser)

      dodge_button = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Уворот", custom_id="buttonDodge")
      block_button = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Блок удара", custom_id="buttonBlock")

      view2 = disnake.ui.View()
      view2.add_item(dodge_button)
      view2.add_item(block_button)
    
      dodge_button.callback = lambda i: button_callback(i,'dodge')
      block_button.callback = lambda i: button_callback(i,'block')
      
      await interaction.response.edit_message('', embed=new_embed, view=view2)

    def make_buttonYes():
      async def buttonYes(interaction: disnake.Interaction):
        if interaction.user.id != user.id:
          # await interaction.send(f"{interaction.user.name}, ход другого игрока!")
          return
       
        new_embed = disnake.Embed(title=f"{interaction.user.display_name}, принял дуэль!", description="Превым будет ходить тот кто вызвал на дуэль!", color=0xffd700)
        new_embed.set_thumbnail(url=interaction.author.display_avatar.url)
        continue_button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Продолжить", custom_id="buttonContinue")
        view = disnake.ui.View()
        view.add_item(continue_button)
        await interaction.response.edit_message('', embed=new_embed, view=view)
        self.contCheck = False
        continue_button.callback = buttonFist
        return continue_button

      yes_button = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Принять", custom_id="buttonYes")
      yes_button.callback = buttonYes
      return yes_button

    def make_buttonNo():
      async def buttonNo(interaction: disnake.Interaction):
        if interaction.user.id != user.id:
          # await interaction.send(f"{interaction.user.name}, ход другого игрока!")
          return

        new_embed = disnake.Embed(title=f"Противник убежал!", description=(f"{interaction.user.display_name}, за побег твоё очко было потеряно!"), color=0xffd700)
        new_embed.set_thumbnail(url=interaction.author.display_avatar.url)
        await interaction.response.edit_message(embed=new_embed, view=None)

      no_button = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Отказаться", custom_id="buttonNo")
      no_button.callback = buttonNo
      return no_button
      
    yes_button = make_buttonYes()
    no_button = make_buttonNo()

    view = disnake.ui.View()
    view.add_item(yes_button)
    view.add_item(no_button)

    await ctx.send(f"{user.mention}, время отстоять свою честь!", embed=embed1, view=view)

def setup(bot):
    bot.add_cog(Duel(bot))
