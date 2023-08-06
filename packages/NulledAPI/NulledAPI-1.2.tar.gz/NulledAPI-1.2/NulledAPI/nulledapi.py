import cloudscraper
from hashlib import md5
scrp = cloudscraper.create_scraper()
class Nulled:
    '''
    NulledAPI is an unofficial [nulled.to](https://www.nulled.to/) API
    to better and more easily integrate features such as
    a ramped up version of nulled auth, and have access to
    useful functions such as searching for users, getting user info
    (much more functions in the works)\n
    It has been created by [M3GZ](https://www.nulled.to/user/4103370-m3gz)
    '''
    group_list = {
        92: 'nova',
        91: 'aqua',
        100: 'disinfector',
        7: 'vip',
        10: 'contributor',
        12: 'royal',
        38: 'legendary',
        102: 'coder',
        99: 'godly',
        8: 'reverser',
        73: 'retired',
        6: 'mod',
        109: 'admin',
        80: 'trialmod',
    }

    def get_user_info(self, user_name_or_id, secure_hash='', session_id=''):
        '''
        Returns dictionary in the format below\n
        Example usage\n
        `print(nulled.get_user_info('brian','secure_hash','session_id'))`\n
        OR\n
        `print(nulled.get_user_info(1468487))`\n
        ```json
        {
            'user_found': True,
            'username': 'Brian',
            'id': 1468487,
            'group': 'disinfector',
            'shouts': 2381,
            'discord': None,
            'error': (False, 'NO_ERROR_USER_FOUND')
        }
        ```
        Go crazy with the information, information is power, especially when it's just one line of code to get it
        
        Parameters<br>
            1. user_name_or_id : str/int
                Description: Use either UID or username
                    UID: Standalone usage
                    Username: You need to put in your session_id and secure_hash
                            (Check notes)
            
            2. secure_hash : str, not required with UID
                Description: Your nulled.to secure_hash
                    UID: Standalone usage
                    Username: You need to put in your secure_hash
                            (Check notes)
            
            3. session_id : str, not required with UID
                Description: Your nulled.to secure_hash
                    UID: Standalone usage
                    Username: You need to put in your latest session_id
                            (Check notes)
        '''
        try:
            user_name_or_id = int(user_name_or_id)
        except ValueError:
            if secure_hash == '':
                return {'user_found':False,'error':(True,'NULL_SECURE_HASH')}
            if session_id == '':
                return {'user_found':False,'error':(True,'NULL_SESSION_ID')}
            try:
                a = self.search_user(user_name_or_id,secure_hash,session_id)
            except ValueError:
                return {'user_found':False,'error':(True,'BAD_SESSION_ID_OR_CF_ERROR')}
            try:
                user_name_or_id = [x for x in a if (a[x]['name'].lower() == user_name_or_id)][0]
            except TypeError:
                return {'user_found':False,'error':(True,'BAD_SESSION_ID')}
        try:
            r = scrp.get('https://chat-ssl2.nulled.to/api/user/'+str(user_name_or_id)).json()['data']['user']
        except ValueError:
            return {'user_found':False,'error':(True,'BANNED_USER_OR_UNDOCUMENTED_CUSTOM_UG_KAPPA')}
        info = {'user_found':True}|dict((k,r[k]) for k in ['username','id','group','shouts','discord'])|{'error':(False,'NO_ERROR_USER_FOUND')}
        info['group'] = self.group_list[info['group']]
        return info

    def auth(self, auth_code:str):
        '''
        Returns dictionary in the format below\n
        Example usage\n
        `print(nulled.auth('NULLED-5E72C-60984-4D332-5B526-X'))`
        ```json
        {
            'authenticated': True,
            'user_found': True,
            'username': 'M3GZ',
            'id': 4103370,
            'group': 'aqua',
            'shouts': 348,
            'discord': '_megz#1304',
            'error': (False, 'NO_ERROR_USER_FOUND')
        }
        ```
        Now you can limit parts of your programs for different usergroups Kappa
        Parameters<br>
            auth_code : str
                Description: Nulled auth code (https://www.nulled.to/auth.php)
        '''

        try:
            r = scrp.get('https://www.nulled.to/misc.php?action=validateKey&authKey='+md5(str.encode(auth_code)).hexdigest()).json()
            if r['auth']:
                return {'authenticated':True}|self.get_user_info(r['uid'])
            else:
                return {'authenticated':False}
        except KeyError:
            return {'authenticated':False}
    
    def search_user(self, username:str, secure_hash:str, session_id:str):
        '''
        Returns dictionary of all similarly named users found\n
        Example usage\n
        `print(nulled.search_user('m3gz','secure_hash','session_id'))`
        ```json
        {
            '4103370': {        #Dict keys are the UIDs
                'name': 'M3GZ',
                'group': 'Aqua',
                'profile_pic': 'https://www.nulled.to/uploads/profile/photo-thumb-4103370.png?_r=1598880866'
            },
            '2515890': {
                'name': 'm3gzz',
                'group': 'Members',
                'profile_pic': 'https://media.nulled.to/public/style_images/images/profile/default_large.png'
            }
        }
        ```
        User search function might be useful to get user-list for various purposes,<br>you could check each user with get_user_info() to get more information
        
        Parameters<br>
            1. username : str
                Description: Username to search
            
            2. secure_hash : str
                Description: Your nulled.to secure_hash
                You need to put in your secure_hash
                (Check notes)
            
            3. session_id : str
                Description: Your nulled.to secure_hash
                You need to put in your latest session_id
                (Check notes)
        '''
        headers = {'cookie':'nulledsession_id='+session_id+';'}
        try:
            a = scrp.get('https://www.nulled.to/index.php?app=core&module=ajax&section=findnames&do=get-member-names&secure_key='+secure_hash+'&name='+username,headers=headers).json()
        except ValueError:
            return {'user_found':False,'error':(True,'BAD_SESSION_ID_OR_CF_ERROR')}
        return dict((k,{'name':a[k]['name'],'group':a[k]['showas'][a[k]['showas'][:a[k]['showas'].rfind('>')].rfind('>')+1:a[k]['showas'].find('<',a[k]['showas'][:a[k]['showas'].rfind('>')].rfind('>')+1)],'profile_pic':a[k]['img']}) for k in a)