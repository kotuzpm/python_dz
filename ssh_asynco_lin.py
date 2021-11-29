import asyncio, asyncssh, sys

async def run_client():
    
    async with asyncssh.connect('51.250.8.136', username='serg', client_keys=['/home/serg/key/private.ppk']) as conn:
    
        result = await conn.run('sudo shutdown -r +1')

        if result.exit_status == 0:
            print(result.stdout, end='')
        else:
            print(result.stderr, end='', file=sys.stderr)
            print('Program exited with status %d' % result.exit_status,
                  file=sys.stderr)

try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))
