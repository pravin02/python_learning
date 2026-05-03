import click

@click.command()
@click.argument("name", type=str)
@click.option("--sort", type=bool)
def main(name, sort):
    print(f"Arguments name: {name}, sort: {sort}")

if __name__ == "__main__":
   main()

#uv run .\args\arg_parser_click_frmk.py --sort=true name=pravin
#uv run .\args\arg_parser_click_frmk.py name=pravin            
#uv run .\args\arg_parser_click_frmk.py name=pravin --sort=False
#uv run .\args\arg_parser_click_frmk.py name=pravin --sort=True 
