#Bot code

#imports
import discord #IMportamos la libreria discord
from discord.ext import commands #De "discord.ext" importamos "commands"
import random #Importamos la libreria random
import os #Importamos "os"
import requests #Importamos requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#//////////////////////////////////////////////Codigo Principal//////////////////////////////////////////////

@bot.event #Nos indica si el bot de ha logeado (iniciado) correctamente
async def on_ready():
    print(f'Se a iniciado sesion correctamente! {bot.user}')


@bot.command() #Codigo del comando "$joined" que puedes utilizar mencionando a la persona que quieras saber cuando ingreso al servidor en el que estas poniendo el comando
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} Se metio al servidor el: {discord.utils.format_dt(member.joined_at)}')


@bot.command() #Codigo del comando "$ubication" que funciona para lanzarte una lista de paises 
async def ubication(ctx):
    await ctx.send(f"Que pais deseas elegir?:")
    await ctx.send(f"$Colombia")
    await ctx.send(f"$Mexico")
    await ctx.send(f"$Chile")
    await ctx.send(f"$Uruguay")
    await ctx.send(f"$Brasil")
    await ctx.send(f"$Argentina")

@bot.command() #Codigo del comando del pais "Colombia"
async def Colombia(ctx):
    await ctx.send(f"En los últimos años, Colombia ha experimentado sequías prolongadas en regiones como La Guajira, donde la escasez de agua ha afectado gravemente a las comunidades locales y la agricultura. Estas sequías son atribuidas en parte al cambio climático y al fenómeno de El Niño, que ha aumentado su intensidad debido al calentamiento global.")

@bot.command() #Codigo del comando del pais "Mexico"
async def Mexico(ctx):
    await ctx.send(f"En los últimos años, México ha experimentado un aumento en la actividad ciclónica en el Golfo de México y el Océano Pacífico, lo que ha resultado en huracanes más frecuentes y poderosos. Estos fenómenos climáticos extremos han causado devastación en varias regiones costeras, provocando inundaciones, deslizamientos de tierra, daños a la infraestructura y pérdidas humanas y económicas significativas.")

@bot.command() #Codigo del comando del pais "Chile"
async def Chile(ctx):
    await ctx.send(f"En los últimos años, Chile ha experimentado temporadas de incendios forestales más prolongadas y destructivas, que han devastado extensas áreas de bosques, pastizales y ecosistemas naturales. Estos incendios han sido alimentados por condiciones climáticas extremas, como altas temperaturas, sequías prolongadas y fuertes vientos, que son consistentes con los patrones asociados al cambio climático.")

@bot.command() #Codigo del comando del pais "Uruguay"
async def Uruguay(ctx):
    await ctx.send(f"En los últimos años, Uruguay ha experimentado un incremento en el número de días con temperaturas extremadamente altas durante los meses de verano. Estas olas de calor han provocado impactos significativos en la salud humana, la agricultura y los ecosistemas naturales.")

@bot.command() #Codigo del comando del pais "Brasil"
async def Brasil(ctx):
    await ctx.send(f"En los últimos años, Brasil ha experimentado un incremento preocupante en la tasa de deforestación en la región amazónica, que es considerada uno de los pulmones del mundo debido a su papel crucial en la absorción de dióxido de carbono y la regulación del clima global.")

@bot.command() #Codigo del comando del pais "Argentina"
async def Argentina(ctx):
    await ctx.send(f"En los últimos años, Argentina ha experimentado una serie de eventos climáticos extremos que han tenido un impacto significativo en la agricultura, la ganadería y la seguridad alimentaria del país. Por un lado, se han registrado sequías prolongadas en regiones como la Pampa Húmeda, que es una de las áreas agrícolas más importantes de Argentina. Estas sequías han afectado la producción de cultivos clave como la soja y el maíz, lo que ha provocado pérdidas económicas para los agricultores y ha exacerbado la inseguridad alimentaria en algunas comunidades.")



@bot.command() #Este es el codigo que hace funcionar el comando "$git" que cuando lo utilizamos nos da el link de el github donde se almacena este bot"
async def git(ctx):
    await ctx.send(f"Hola, mi nombre es: {bot.user}, y te dare el link de mi codigo por si me quieres conocer mas a fondo! aqui te dejo el link: https://github.com/ker0sn/proyect/tree/main")

@bot.command() #Este es el codigo que hace funcionar el comando "$hello" que cuando los ponemos en el chat nos dice: "Hola, mi nombre es: our world is dying" y nos da una breve descripcion de para que sirve.
async def hello(ctx):
    await ctx.send(f"Hola, mi nombre es: {bot.user}, y te dire para que sirvo. Soy un bot que intenta incitar al cuidado de nuestro hogar, el planeta Tierra y cuidar todo lo que nos rodea!")

@bot.command() #Codigo del comando "$book" que envia a tu servidor de discord un libro sobre el medioambiente junto a su link de compra.
async def book(ctx):
    await ctx.send(random.choice(["The Sixth Extinction: An Unnatural History por Elizabeth Kolbert, aqui dejo link de compra: https://www.amazon.com/Sixth-Extinction-Unnatural-History/dp/1250062187","This Changes Everything: Capitalism vs. The Climate por Naomi Klein, aqui dejo el link de compra: https://www.amazon.com/This-Changes-Everything-Capitalism-Climate/dp/1451697392","The Uninhabitable Earth: Life After Warming por David Wallace-Wells, aqui dejo el link de compra: https://www.amazon.com/Uninhabitable-Earth-Life-After-Warming/dp/0525576703","Silent Spring por Rachel Carson, aqui dejo el link de compra: https://www.amazon.com/Silent-Spring-Rachel-Carson/dp/0618249060","Drawdown: The Most Comprehensive Plan Ever Proposed to Reverse Global Warming por Paul Hawken, aqui dejo el link de compra: https://www.amazon.com/Drawdown-Comprehensive-Proposed-Reverse-Warming/dp/0143130447","The Water Will Come: Rising Seas, Sinking Cities, and the Remaking of the Civilized World por Jeff Goodell, aqui dejo el link de compra: https://www.amazon.com/Water-Will-Come-Rising-Civilized/dp/031626024X","Eaarth: Making a Life on a Tough New Planet por Bill McKibben, aqui dejo el link de compra: https://www.amazon.com/Eaarth-Making-Life-Tough-Planet/dp/0312541198","Climate Leviathan: A Political Theory of Our Planetary Future por Joel Wainwright y Geoff Mann, aqui dejo el link de compra: https://www.amazon.com/Climate-Leviathan-Political-Theory-Planetary/dp/1786634295","The Great Derangement: Climate Change and the Unthinkable por Amitav Ghosh, aqui dejo link de compra: https://www.amazon.com/Great-Derangement-Climate-Unthinkable-Changes/dp/022632303X","Storms of My Grandchildren: The Truth About the Coming Climate Catastrophe and Our Last Chance to Save Humanity por James Hansen, aqui dejo link de compra: https://www.amazon.com/Storms-My-Grandchildren-Catastrophe-Humanity/dp/1608192008","The End of Nature por Bill McKibben, aqui dejo el link de compra: https://www.amazon.com/End-Nature-Bill-McKibben/dp/0812976088","Braiding Sweetgrass: Indigenous Wisdom, Scientific Knowledge and the Teachings of Plants por Robin Wall Kimmerer, aqui dejo el link de compra: https://www.amazon.com/Braiding-Sweetgrass-Indigenous-Scientific-Knowledge/dp/1571313567","The Future We Choose: Surviving the Climate Crisis por Christiana Figueres y Tom Rivett-Carnac, aqui dejo el link de compra: https://www.amazon.com/Future-We-Choose-Surviving-Climate/dp/0525658351","The Hidden Life of Trees: What They Feel, How They Communicate – Discoveries from a Secret World por Peter Wohlleben, aqui dejo el link de compra: https://www.amazon.com/Hidden-Life-Trees-Communicate_Discoveries/dp/1771642483","The Nature Fix: Why Nature Makes Us Happier, Healthier, and More Creative por Florence Williams, aqui dejo el link de compra: https://www.amazon.com/Nature-Fix-Happier-Healthier-Creative/dp/0393242714"]))

@bot.command() #Codigo del comando "$notice" que envia a tu servidor de discord una noticia sobre el medio ambiente
async def notice(ctx):
    await ctx.send(random.choice(["Las inundaciones causadas por las precipitaciones y el desbordamiento de ríos en el sur de Brasil han dejado un nivel de devastación sin precedentes que ya ha cobrado al menos 100 fallecidos, mientras que más 130 personas continúan desaparecidas.","Casi la mitad de las principales ciudades de China se están hundiendo debido a la extracción de agua y al peso cada vez mayor de su veloz expansión, dicen investigadores.","“Por favor ahorremos agua, la situación es crítica”, escribió este jueves el alcalde de Bogotá, Carlos Fernando Galánen Twitter, por la falta de agua debido a los bajos niveles de los embalses de Bogota, Colombia","Por primera vez, el calentamiento global ha superado los 1,5°C durante todo un año, según el servicio climático de la Unión Europea (UE).","notice1","notice2","notice3","notice4","notice5","notice6","notice7","notice8"]))

@bot.command() #Codigo del comando "$tips" que envia a tu servidor de discord un consejo sobre como evitar la contaminacion en el planeta tierra
async def tips(ctx):
    await ctx.send(random.choice(["Un consejo que te puedo dar para poder evitar la contaminacion del planeta seria: No botar chicles en la calle", "Recicla toda la basura que puedas o reutilizarla para fabricar algun objeto o algo por el estilo", "Usa productos que puedan reutilizarse", "Cuando llueva y quieras regar tus plantas, pon una cubeta de agua para recolectar el agua de la lluvia", "Siempre apaga cualquier dispositivo electronico cuando no los estes usando, y tambien apagar las luces que no se esten usando", "Consume productos ecológicos y locales", "Evita dejar los aparatos enchufados", "Cerrar los grifos correctamente para que no corra el agua y evitar el mal gasto", "Siempre cuando puedas evita usar automovil que usen gasolina y usa bicicleta para evitar contaminar", "Tener siempre en casa distintos tachos de basura para botellas, plasticos, cajas, etc etc etc"]))

@bot.command() #Codigo del comando "$videos" que envia a tu servidor de discord un video sobre el medio ambiente, la contaminacion, y el cambio climatico en el planeta tierra
async def videos(ctx):
    await ctx.send(random.choice(["Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/1yz0-bEqKLY?si=jU2XcJcvy4JgLZpk", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/bR2X6sqsAiY?si=uDRqkU903lPb5HMQ", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/5w8cxYdLcCM?si=Nv9xAIoUJJEUmueM", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/e5y7FMCZwKQ?si=2za7P8oo5nlvY1-t"]))

#//////////////////////////////////////////////Codigo Principal//////////////////////////////////////////////

bot.run("TU TOKEN") #Codigo donde tienes que colocar el token de tu bot para que funcione!