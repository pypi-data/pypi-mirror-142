'Twitch api enums.'
from __future__ import annotations

from twitch_enums_extensions import API, Enum

__all__ = (
    'Scope',
    'Api',
)
__version__ = '1.0.0'
__author__ = 'notory'

class Api(Enum):
    start_commercial = API('https://api.twitch.tv/helix/channels/commercial', 'POST')
    
    get_extension_analytics = API('https://api.twitch.tv/helix/analytics/extensions', 'GET')
    get_game_analytics = API('https://api.twitch.tv/helix/analytics/games?game_id={}&started_at={}&ended_at={}', 'GET')
    get_bits_leaderboard = API('https://api.twitch.tv/helix/bits/leaderboard?count={}&period={}', 'GET')
    get_cheeremotes = API('https://api.twitch.tv/helix/bits/cheeremotes', 'GET')
    get_extension_transactions = API('https://api.twitch.tv/helix/extensions/transactions?extension_id={}', 'GET')
    get_channel_information = API('https://api.twitch.tv/helix/extensions/channels?broadcaster_id={}', 'GET')
    
    modify_channel_information = API('https://api.twitch.tv/helix/channels?broadcaster_id={}', 'PATCH')

    get_channel_editors = API('https://api.twitch.tv/helix/channels/editors?broadcaster_id={}', 'GET')

    create_custom_rewards = API('https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={}', 'POST')

    delete_custom_reward = API('https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={}&id={}', 'DELETE')

    get_custom_reward = API('https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={}', 'GET')
    get_custom_reward_redemption = API('https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={}&reward_id={}&status={}', 'GET')

    update_custom_reward = API('https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={}', 'PATCH')
    update_redemption_status = API('https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={}&reward_id={}', 'PATCH')

    get_channel_emotes = API('https://api.twitch.tv/helix/chat/emotes?broadcaster_id={}', 'GET')
    get_global_emotes = API('https://api.twitch.tv/helix/chat/emotes/global', 'GET')
    get_emote_sets = API('https://api.twitch.tv/helix/chat/emotes/set?emote_set_id={}', 'GET')
    get_channel_chat_badges = API('https://api.twitch.tv/helix/chat/badges?broadcaster_id={}', 'GET')
    get_global_chat_badges = API('https://api.twitch.tv/helix/chat/badges/global', 'GET')
    get_chat_settings = API('https://api.twitch.tv/helix/chat/settings?broadcaster_id={}', 'GET')
    
    update_chat_settings = API('https://api.twitch.tv/helix/chat/settings?broadcaster_id={}&moderator_id={}', 'PATCH')

    create_clip = API('https://api.twitch.tv/helix/clips?broadcaster_id={}', 'POST')
    
    get_clips = API('https://api.twitch.tv/helix/clips?id=AwkwardHelplessSalamanderSwiftRage', 'GET')
    get_code_status = API('https://api.twitch.tv/helix/entitlements/codes?code={}&user_id={}', 'GET')
    get_drops_entitlements = API('https://api.twitch.tv/helix/entitlements/drops?user_id={}&game_id={}', 'GET')

    update_drops_entitlements = API('https://api.twitch.tv/helix/entitlements/drops', 'UPDATE')

    redeem_code = API('https://api.twitch.tv/helix/entitlements/codes?code={}&code={}', 'POST')

    get_extension_configuration_segment = API('https://api.twitch.tv/helix/extensions/configurations?extension_id={}&segment={}', 'GET')

    set_extension_configuration_segment = API('https://api.twitch.tv/helix/extensions/configurations', 'PUT')
    set_extension_required_configuration = API('https://api.twitch.tv/helix/extensions/required_configuration?broadcaster_id={}', 'PUT')

    send_extension_pubsub_message = API('https://api.twitch.tv/helix/extensions/pubsub', 'POST')
    
    get_extension_live_channels = API('https://api.twitch.tv/helix/extensions/live?extension_id={}', 'GET')
    get_extension_secrets = API('https://api.twitch.tv/helix/extensions/jwt/secrets?extension_id={}', 'GET')

    create_extension_secret = API('https://api.twitch.tv/helix/extensions/jwt/secrets?extension_id={}&delay={}', 'POST')

    send_extension_chat_message = API('https://api.twitch.tv/helix/extensions/chat?broadcaster_id={}', 'POST')
    
    get_extensions = API('https://api.twitch.tv/helix/extensions?extension_id={}&extension_version={}', 'GET')
    get_released_extensions = API('https://api.twitch.tv/helix/extensions/released?extension_version={}&extension_id={}', 'GET')
    get_extension_bits_product = API('https://api.twitch.tv/helix/bits/extensions?should_include_all={}', 'GET')

    update_extension_bits_product = API('https://api.twitch.tv/helix/bits/extensions', 'PUT')
    
    create_eventsub_subscription = API('https://api.twitch.tv/helix/eventsub/subscriptions', 'POST')

    delete_eventsub_subscription = API('https://api.twitch.tv/helix/eventsub/subscriptions?id={}', 'DELETE')

    get_eventsub_subscriptions = API('https://api.twitch.tv/helix/eventsub/subscriptions', 'GET')
    get_top_games = API('https://api.twitch.tv/helix/games/top', 'GET')
    get_games = API('https://api.twitch.tv/helix/games?id={}', 'GET')
    get_creator_goals = API('https://api.twitch.tv/helix/goals?broadcaster_id={}', 'GET')
    get_hype_train_events = API('https://api.twitch.tv/helix/hypetrain/events?broadcaster_id={}&first={}', 'GET')

    check_automod_status = API('https://api.twitch.tv/helix/moderation/enforcements/status', 'POST')

    manage_held_automod_messages = API('https://api.twitch.tv/helix/moderation/automod/message', 'POST')

    get_automod_settings = API('https://api.twitch.tv/helix/moderation/automod/settings?broadcaster_id={}&moderator_id={}', 'GET')
    
    update_automod_settings = API('https://api.twitch.tv/helix/moderation/automod/settings?broadcaster_id={}&moderator_id={}', 'PUT')

    get_banned_events = API('https://api.twitch.tv/helix/moderation/banned/events?broadcaster_id={}', 'GET')
    get_banned_users = API('https://api.twitch.tv/helix/moderation/banned?broadcaster_id={}', 'GET')

    ban_user = API('https://api.twitch.tv/helix/moderation/bans?broadcaster_id={}&moderator_id={}', 'POST')
    unban_user = API('https://api.twitch.tv/helix/moderation/bans?broadcaster_id={}&moderator_id={}&user_id={}', 'DELETE')
    
    get_blocked_terms = API('https://api.twitch.tv/helix/moderation/blocked_terms?broadcaster_id={}&moderator_id={}&first={}', 'GET')

    add_blocked_term = API('https://api.twitch.tv/helix/moderation/blocked_terms?broadcaster_id={}&moderator_id={}', 'POST')
    
    remove_blocked_term = API('https://api.twitch.tv/helix/moderation/blocked_terms?broadcaster_id={}&moderator_id={}&id={}', 'DELETE')

    get_moderators = API('https://api.twitch.tv/helix/moderation/moderators?broadcaster_id={}', 'GET')
    get_polls = API('https://api.twitch.tv/helix/polls?broadcaster_id={}&id={}', 'GET')
    
    create_poll = API('https://api.twitch.tv/helix/polls', 'POST')

    end_poll = API('https://api.twitch.tv/helix/polls', 'PATCH')
    
    get_predections = API('https://api.twitch.tv/helix/predictions?broadcaster_id={}&id={}', 'GET')

    create_prediction = API('https://api.twitch.tv/helix/predictions', 'POST')

    end_predection = API('https://api.twitch.tv/helix/predictions', 'PATCH')

    get_channel_stream_schedule = API('https://api.twitch.tv/helix/schedule?broadcaster_id={}', 'GET')
    get_channel_icalandar = API('https://api.twitch.tv/helix/schedule/icalendar?broadcaster_id={}', 'GET')

    update_channel_stream_schedule = API('https://api.twitch.tv/helix/schedule/settings?broadcaster_id={}&is_vacation_enabled={}&vacation_start_time={}&vacation_end_time={}&timezone={}', 'PATCH')

    create_channel_stream_schedule_segment = API('https://api.twitch.tv/helix/schedule/segment?broadcaster_id={}', 'POST')
    
    update_channel_stream_schedule_segment = API('https://api.twitch.tv/helix/schedule/segment?broadcaster_id={}&id={}', 'PATCH')
    
    delete_channel_stream_schedule_segment = API('https://api.twitch.tv/helix/schedule/segment?broadcaster_id={}&id={}', 'DELETE')

    search_categories = API('https://api.twitch.tv/helix/search/categories?query={}', 'GET')
    search_channels = API('https://api.twitch.tv/helix/search/channels?query={}', 'GET')
    
    get_soundtrack_current_track = API('https://api.twitch.tv/helix/soundtrack/current_track?broadcaster_id={}', 'GET')
    get_soundtrack_playlist = API('https://api.twitch.tv/helix/soundtrack/playlist?id={}', 'GET')
    get_soundtrack_playlists = API('https://api.twitch.tv/helix/soundtrack/playlists', 'GET')
    get_stream_key = API('https://api.twitch.tv/helix/streams/key', 'GET')
    get_streams = API('https://api.twitch.tv/helix/streams', 'GET')
    get_followed_streams = API('https://api.twitch.tv/helix/streams/followed?user_id={}', 'GET')

    create_stream_marker = API('https://api.twitch.tv/helix/streams/markers', 'POST')
    
    get_stream_markers = API('https://api.twitch.tv/helix/streams/markers?user_id={}&first={}', 'GET')
    get_broadcaster_subscriptions = API('https://api.twitch.tv/helix/subscriptions?broadcaster_id={}', 'GET')

    check_user_subscription = API('https://api.twitch.tv/helix/subscriptions/user?broadcaster_id={}&user_id={}', 'GET')

    get_all_stream_tags = API('https://api.twitch.tv/helix/tags/streams', 'GET')
    get_stream_tags = API('https://api.twitch.tv/helix/streams/tags?broadcaster_id={}', 'GET')

    replace_stream_tags = API('https://api.twitch.tv/helix/streams/tags?broadcaster_id={}', 'PUT')

    get_channel_teams = API('https://api.twitch.tv/helix/teams/channel?broadcaster_id={}', 'GET')
    get_teams = API('https://api.twitch.tv/helix/teams?id={}', 'GET')
    get_users = API('https://api.twitch.tv/helix/users?id={}', 'GET')

    update_user = API('https://api.twitch.tv/helix/users?description={}', 'PUT')

    get_user_follows = API('https://api.twitch.tv/helix/users/follows?to_id={}', 'GET')
    get_user_block_list = API('https://api.twitch.tv/helix/users/blocks?broadcaster_id={}', 'GET')

    block_user = API('https://api.twitch.tv/helix/users/blocks?target_user_id={}', 'PUT')

    unblock_user = API('https://api.twitch.tv/helix/users/blocks?target_user_id={}', 'DELETE')
    
    get_user_extensions = API('https://api.twitch.tv/helix/users/extensions/list', 'GET')
    get_user_active_extensions = API('https://api.twitch.tv/helix/users/extensions', 'GET')
    
    update_user_extensions = API('https://api.twitch.tv/helix/users/extensions', 'PUT')

    get_videos = API('https://api.twitch.tv/helix/videos?id={}', 'GET')
    
    delete_videos = API('https://api.twitch.tv/helix/videos?{}', 'DELETE')

class Scope(Enum):
    analytics_read_extensions = 'analytics:read:extensions'
    analytics_read_games = 'analytics:read:games'
    
    bits_read = 'bits:read'

    channel_edit_commercial = 'channel:edit:commercial'
    channel_manage_broadcast = 'channel:manage:broadcast'
    channel_manage_extensions = 'channel:manage:extensions'
    channel_manage_polls = 'channel:manage:polls'
    channel_manage_predictions = 'channel:manage:predictions'
    channel_manage_redemptions = 'channel:manage:redemptions'
    channel_manage_schedule = 'channel:manage:schedule'
    channel_manage_videos = 'channel:manage:videos'
    channel_read_editors = 'channel:read:editors'
    channel_read_goals = 'channel:read:goals'
    channel_read_hype_train = 'channel:read:hype_train'
    channel_read_polls = 'channel:read:polls'
    channel_read_predictions = 'channel_read_predictions'
    channel_read_redemptions = 'channel_read_redemptions'
    channel_read_stream_key = 'channel:read:stream_key'
    channel_read_subscriptions = 'channel:read:subscriptions'

    clips_edit = 'clips:edit'

    moderation_read = 'moderation:read'
    moderator_manage_banned_users = 'moderator:manage:banned_users'
    moderator_read_blocked_terms = 'moderator:read:blocked_terms'
    moderator_manage_blocked_terms = 'moderator:manage:blocked_terms'
    moderator_manage_automod = 'moderator:manage:automod'
    moderator_read_automod_settings = 'moderator:read:automod_settings'
    moderator_read_chat_settings = 'moderator:read:chat_settings'

    user_edit = 'user:edit'
    user_edit_follows = 'user:edit:follows'
    user_manage_blocked_users = 'user:manage:blocked_users'
    user_read_blocked_users = 'user:read:blocked_users'
    user_read_broadcast = 'user:read:broadcast'
    user_read_email = 'user:read:email'
    user_read_follows = 'user:read:follows'
    user_read_subscriptions = 'user:read:subscriptions'

if __name__ == '__main__':
    print(set(Api.as_list))
    print(set(Scope.as_list))