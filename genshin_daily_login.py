import asyncio
import logging
import argparse
import genshin
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('genshin_login.log'),
        logging.StreamHandler()
    ]
)

async def claim_daily_reward(username: str, password: str, game: str):
    """
    Claims the daily reward for the specified game using the genshin.py library
    """
    try:
        # Map game string to genshin.Game enum
        game_map = {
            'genshin': genshin.Game.GENSHIN,
            'zzz': genshin.Game.ZZZ
        }
        
        if game.lower() not in game_map:
            raise ValueError(f"Invalid game specified. Must be one of: {', '.join(game_map.keys())}")
        
        # Create client with specified game
        client = genshin.Client(game=game_map[game.lower()])
        
        # Login with username and password
        logging.info(f"Attempting to log in to {game}...")
        await client.login_with_password(username, password)
        logging.info(f"Login successful for {game}")

        # Claim daily reward
        logging.info(f"Attempting to claim daily reward for {game}...")
        reward = await client.claim_daily_reward()
        logging.info(f"Successfully claimed daily reward: {reward.amount}x {reward.name}")
        return True

    except genshin.InvalidCookies:
        logging.error("Invalid login credentials")
        return False
    except genshin.AlreadyClaimed:
        logging.info(f"Daily reward already claimed today for {game}")
        return True
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False

def main():
    """
    Main function to parse arguments and claim the daily reward
    """
    parser = argparse.ArgumentParser(description="HoYoLAB Daily Login Reward Claimer")
    parser.add_argument("username", help="HoYoLAB account username")
    parser.add_argument("password", help="HoYoLAB account password")
    parser.add_argument("--game", default="genshin", choices=["genshin", "zzz"],
                      help="Game to claim daily reward for (default: genshin)")

    args = parser.parse_args()

    # Run the async function
    try:
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        success = asyncio.run(claim_daily_reward(args.username, args.password, args.game))
        
        if success:
            print(f"Daily login check-in completed successfully for {args.game}")
            sys.exit(0)
        else:
            print(f"Daily login check-in failed for {args.game}")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)

if __name__ == "__main__":
    main()