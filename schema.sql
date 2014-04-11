BEGIN;
CREATE TABLE "idb_mvp" (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(500) NOT NULL,
    "last_name" varchar(500) NOT NULL,
    "position" varchar(4) NOT NULL,
    "birth_date" date NOT NULL,
    "birth_town" varchar(500) NOT NULL,
    "high_school" varchar(500) NOT NULL,
    "college" varchar(500) NOT NULL,
    "draft_year" integer NOT NULL,
    "active" boolean NOT NULL,
    "salary" integer NOT NULL,
    "facebook_id" varchar(500) NOT NULL,
    "twitter_id" varchar(500) NOT NULL,
    "youtube_id" varchar(500) NOT NULL,
    "latitude" double precision NOT NULL,
    "longitude" double precision NOT NULL
)
;
CREATE TABLE "idb_franchise_mvps" (
    "id" serial NOT NULL PRIMARY KEY,
    "franchise_id" integer NOT NULL,
    "mvp_id" integer NOT NULL REFERENCES "idb_mvp" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("franchise_id", "mvp_id")
)
;
CREATE TABLE "idb_franchise" (
    "id" serial NOT NULL PRIMARY KEY,
    "team_name" varchar(500) NOT NULL,
    "team_city" varchar(500) NOT NULL,
    "team_state" varchar(2) NOT NULL,
    "current_owner" varchar(500) NOT NULL,
    "current_gm" varchar(500) NOT NULL,
    "current_head_coach" varchar(500) NOT NULL,
    "year_founded" integer NOT NULL,
    "active" boolean NOT NULL,
    "home_stadium" varchar(500) NOT NULL,
    "division" varchar(500) NOT NULL,
    "facebook_id" varchar(500) NOT NULL,
    "twitter_id" varchar(500) NOT NULL,
    "youtube_id" varchar(500) NOT NULL,
    "latitude" double precision NOT NULL,
    "longitude" double precision NOT NULL
)
;
ALTER TABLE "idb_franchise_mvps" ADD CONSTRAINT "franchise_id_refs_id_0a0fbb98" FOREIGN KEY ("franchise_id") REFERENCES "idb_franchise" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE "idb_superbowl" (
    "id" serial NOT NULL PRIMARY KEY,
    "winning_franchise_id" integer NOT NULL REFERENCES "idb_franchise" ("id") DEFERRABLE INITIALLY DEFERRED,
    "losing_franchise_id" integer NOT NULL REFERENCES "idb_franchise" ("id") DEFERRABLE INITIALLY DEFERRED,
    "mvp_id" integer NOT NULL REFERENCES "idb_mvp" ("id") DEFERRABLE INITIALLY DEFERRED,
    "mvp_stats" varchar(500) NOT NULL,
    "mvp_blurb" varchar(500) NOT NULL,
    "winning_score" integer NOT NULL,
    "losing_score" integer NOT NULL,
    "venue_name" varchar(500) NOT NULL,
    "venue_city" varchar(500) NOT NULL,
    "venue_state" varchar(500) NOT NULL,
    "game_day" date NOT NULL,
    "attendance" integer NOT NULL,
    "game_number" varchar(500) NOT NULL,
    "halftime_performer" varchar(500) NOT NULL,
    "twitter_id" varchar(500) NOT NULL,
    "youtube_id" varchar(500) NOT NULL,
    "latitude" double precision NOT NULL,
    "longitude" double precision NOT NULL
)
;
CREATE INDEX "idb_franchise_mvps_franchise_id" ON "idb_franchise_mvps" ("franchise_id");
CREATE INDEX "idb_franchise_mvps_mvp_id" ON "idb_franchise_mvps" ("mvp_id");
CREATE INDEX "idb_superbowl_winning_franchise_id" ON "idb_superbowl" ("winning_franchise_id");
CREATE INDEX "idb_superbowl_losing_franchise_id" ON "idb_superbowl" ("losing_franchise_id");
CREATE INDEX "idb_superbowl_mvp_id" ON "idb_superbowl" ("mvp_id");

COMMIT;
