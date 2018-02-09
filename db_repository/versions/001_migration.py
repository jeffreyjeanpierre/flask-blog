from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
album = Table('album', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=20)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

image = Table('image', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('image', LargeBinary),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('post_body', String(length=500)),
)

tags = Table('tags', post_meta,
    Column('tag_id', Integer),
    Column('post_id', Integer),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('rebin', String(length=5)),
    Column('hidden', String(length=5)),
    Column('body', String(length=500)),
    Column('title', String(length=32)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('album_id', Integer),
    Column('rating', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['album'].create()
    post_meta.tables['image'].create()
    post_meta.tables['tags'].create()
    post_meta.tables['post'].columns['album_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['album'].drop()
    post_meta.tables['image'].drop()
    post_meta.tables['tags'].drop()
    post_meta.tables['post'].columns['album_id'].drop()
