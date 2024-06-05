"""preparing db for new book

Revision ID: ff52779919c5
Revises: 23aa591d3215
Create Date: 2024-06-04 15:18:13.767994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ff52779919c5"
down_revision: Union[str, None] = "23aa591d3215"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "book",
        sa.Column("page_id", sa.Integer(), nullable=False),
        sa.Column("page_text", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("page_id"),
    )
    op.create_table(
        "dictionary",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("term", sa.String(length=64), nullable=False),
        sa.Column("translation", sa.String(length=64), nullable=True),
        sa.Column("definition", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("psalter_psalms")
    op.drop_table("min_book")
    op.drop_table("min_fragments")
    op.drop_table("eng_book")
    op.drop_table("new_words_dictionary")
    op.drop_table("joke")
    op.drop_table("psalter_pages")
    op.drop_table("kabdictionary")
    op.add_column(
        "users",
        sa.Column("current_book_page", sa.Integer(), server_default="1", nullable=False),
    )
    op.drop_column("users", "current_mn_page")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("current_mn_page", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("users", "current_book_page")
    op.create_table(
        "kabdictionary",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("term", sa.VARCHAR(length=64), autoincrement=False, nullable=False),
        sa.Column(
            "translation", sa.VARCHAR(length=64), autoincrement=False, nullable=True
        ),
        sa.Column("definition", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="kabdictionary_pkey"),
    )
    op.create_table(
        "psalter_pages",
        sa.Column("page_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("psalm_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("psalm_text", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("page_id", name="psalter_pages_pkey"),
    )
    op.create_table(
        "joke",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("joke", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column(
            "user_name", sa.VARCHAR(length=32), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name="joke_pkey"),
    )
    op.create_table(
        "new_words_dictionary",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("term", sa.VARCHAR(length=64), autoincrement=False, nullable=False),
        sa.Column(
            "translation", sa.VARCHAR(length=64), autoincrement=False, nullable=True
        ),
        sa.Column("definition", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="new_words_dictionary_pkey"),
        sa.UniqueConstraint("term", name="new_words_dictionary_term_key"),
    )
    op.create_table(
        "eng_book",
        sa.Column("page_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("page_text", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("page_id", name="eng_book_pkey"),
    )
    op.create_table(
        "min_fragments",
        sa.Column("fragment_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("fragment", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("fragment_id", name="min_fragments_pkey"),
    )
    op.create_table(
        "min_book",
        sa.Column("page_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("fragment_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("page_text", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("page_id", name="min_book_pkey"),
    )
    op.create_table(
        "psalter_psalms",
        sa.Column("psalm_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("psalm_text", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("psalm_id", name="psalter_psalms_pkey"),
    )
    op.drop_table("dictionary")
    op.drop_table("book")
    # ### end Alembic commands ###