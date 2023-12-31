
from enum import IntEnum
from typing import List, Dict
from api.Maps import Maps
from pydantic import BaseModel, field_validator, model_serializer
from typing import Optional

VERSION = 12


def get_class_by_name(class_name: str):
    # Use the globals() function to access the global namespace
    global_namespace = globals()

    # Check if the class exists in the global namespace
    if class_name in global_namespace:
        return global_namespace[class_name]
    else:
        raise ValueError(f"Class '{class_name}' not found")


class Upgrade(IntEnum):
    U0 = 0,
    U1 = 1000000,
    U2 = 2000000,
    U3 = 3000000,


type CardId = int
"""
 ID of the card resource
"""


type SquadId = int
"""
 ID of squad resource
"""


type BuildingId = int
"""
 ID of building resource
"""


type SpellId = int
"""
 ID of spell resource
"""


type AbilityId = int
"""
 ID of ability resource
"""


type ModeId = int
"""
 ID of mode resource
"""


type EntityId = int
"""
 ID of an entity present in the match unique to that match
 First entity have ID 1, next 2, ...
 Ids are never reused
"""


class CommunityMapInfo(BaseModel):
    name: str
    """
     Name of the map.
    """
    crc: int
    """
     Checksum of them map.
    """


class MapInfo(BaseModel):
    """
     Official spectator maps are normal maps (have unique id) so only `map` field is needed.
    """
    map: Maps
    """
     Represents the map, unfortunately EA decided, it will be harder for community maps.
    """
    community_map_details: Optional[CommunityMapInfo] = None
    """
     Is relevant only for community maps.
    """


class DeckAPI(BaseModel):
    name: str
    """
     Name of the deck, must be unique across decks used by bot, but different bots can have same deck names.
     Must not contain spaces, to be addable in game.
    """
    cover_card_index: int
    """
     Index of a card that will be deck icon 0 to 19 inclusive
    """
    cards: List[CardId]
    """
     List of 20 cards in deck.
     Fill empty spaces with `NotACard`.
    """


class AbilityLine(IntEnum):
    _EAsBug_betterSafeThanSorry = 0,
    ModifyWalkSpeed = 1,
    UnControllable = 4,
    UnKillable = 5,
    UnAttackable = 9,
    HitMultiple = 10,
    _ACModifier = 14,
    DamageOverTime = 15,
    DamageBuff = 21,
    PowerOutputModifier = 23,
    MoveSpeedOverwrite = 24,
    HitMultipleRanged = 25,
    HPModifier = 26,
    Aura = 27,
    PreventCardPlay = 29,
    _SpreadFire = 31,
    _SquadSpawnZone = 32,
    HitMultipleProjectile = 33,
    _MarkedTargetDamageMultiplier = 36,
    _MarkedTargetDamage = 37,
    _AttackPauseDelay = 39,
    _MarkedForTeleport = 40,
    _RangeModifier = 41,
    ForceAttack = 42,
    OnEntityDie = 44,
    _FireLanceAbility = 47,
    Collector = 50,
    _ChangeTargetAggro = 51,
    _FireLanceBurstCollector = 53,
    RegenerationOld = 54,
    _TimedSpell = 57,
    Scatter = 58,
    _DamageOverTimeNoCombat = 59,
    LifeStealer = 60,
    BarrierGate = 61,
    GlobalRevive = 62,
    TrampleResistance = 64,
    TrampleOverwrite = 65,
    PushbackResistance = 66,
    MeleePushbackOverride = 67,
    _FanCollector = 69,
    MeleeFightSpeedModifier = 71,
    _SpellRangeModifierIncoming = 72,
    SpellRangeModifierOutgoing = 73,
    _FanCollectorBurst = 74,
    RangedFightSpeedModifier = 75,
    _SquadRestore = 76,
    DamagePowerTransfer = 79,
    TimedSpell = 80,
    TrampleRevengeDamage = 81,
    LinkedFire = 83,
    DamageBuffAgainst = 84,
    IncomingDamageModifier = 85,
    GeneratorPower = 86,
    IceShield = 87,
    DoTRefresh = 88,
    EnrageThreshold = 89,
    Immunity = 90,
    _UnitSpawnZone = 91,
    Rage = 92,
    _PassiveCharge = 93,
    MeleeHitSpell = 95,
    _FireDebuff = 97,
    FrostDebuff = 98,
    SpellBlocker = 100,
    ShadowDebuff = 102,
    SuicidalBomb = 103,
    GrantToken = 110,
    TurretCannon = 112,
    SpellOnSelfCast = 113,
    AbilityOnSelfResolve = 114,
    SuppressUserCommand = 118,
    LineCast = 120,
    NoCheer = 132,
    UnitShredderJobCondition = 133,
    DamageRadialArea = 134,
    _DamageConeArea = 137,
    DamageConeCutArea = 138,
    ConstructionRepairModifier = 139,
    Portal = 140,
    Tunnel = 141,
    ModeConditionDelay = 142,
    HealAreaRadial = 144,
    _145LeftoverDoesNotReallyExistButIsUsed = 145,
    _146LeftoverDoesNotReallyExistButIsUsed = 146,
    OverrideWeaponType = 151,
    DamageRadialAreaUsingCorpse = 153,
    HealAreaRadialInstantContinues = 154,
    ChargeableBombController = 155,
    ChargeAttack = 156,
    ChargeableBomb = 157,
    ModifyRotationSpeed = 159,
    ModifyAcceleration = 160,
    FormationOverwrite = 161,
    EffectHolder = 162,
    WhiteRangersHomeDefenseTrigger = 163,
    _167LeftoverDoesNotReallyExistButIsUsed = 167,
    _168LeftoverDoesNotReallyExistButIsUsed = 168,
    HealReservoirUsingCorpse = 170,
    ModeChangeBlocker = 171,
    BarrierModuleEnterBlock = 172,
    ProduceAmmoUsingCorpseInjurity = 173,
    IncomingDamageSpreadOnTargetAlignmentArea1 = 174,
    DamageSelfOnMeleeHit = 175,
    HealthCapCurrent = 176,
    ConstructionUnCrushable = 179,
    ProduceAmmoOverTime = 180,
    BarrierSetBuildDelay = 181,
    ChannelTimedSpell = 183,
    AuraOnEnter = 184,
    ParalyzeAbility = 185,
    IgnoreSummoningSickness = 186,
    BlockRepair = 187,
    Corruption = 188,
    UnHealable = 189,
    Immobile = 190,
    ModifyHealing = 191,
    IgnoreInCardCondition = 192,
    MovementMode = 193,
    ConsumeAmmoHealSelf = 195,
    ConsumeAmmoHealAreaRadial = 196,
    CorpseGather = 197,
    AbilityNearEntity = 198,
    ModifyIceShieldDecayRate = 200,
    ModifyDamageIncomingAuraContingentSelfDamage = 201,
    ModifyDamageIncomingAuraContingentSelfDamageTargetAbility = 202,
    ConvertCorpseToPower = 203,
    EraseOverTime = 204,
    FireStreamChannel = 205,
    DisableMeleeAttack = 206,
    AbilityOnPlayer = 207,
    GlobalAbilityOnEntity = 208,
    AuraModifyCardCost = 209,
    AuraModifyBuildTime = 210,
    GlobalRotTimeModifier = 211,
    _212LeftoverDoesNotReallyExistButIsUsed = 212,
    MindControl = 213,
    SpellOnEntityNearby = 214,
    AmmoConsumeModifyIncomingDamage = 216,
    AmmoConsumeModifyOutgoingDamage = 217,
    GlobalSuppressRefund = 219,
    DirectRefundOnDie = 220,
    OutgoingDamageDependendSpell = 221,
    DeathCounter = 222,
    DeathCounterController = 223,
    DamageRadialAreaUsingGraveyard = 224,
    MovingIntervalCast = 225,
    BarrierGateDelay = 226,
    EffectHolderAmmo = 227,
    FightDependentAbility = 228,
    GlobalIgnoreCardPlayConditions = 229,
    WormMovement = 230,
    DamageRectAreaAligned = 231,
    GlobalRefundOnEntityDie = 232,
    GlobalDamageAbsorption = 233,
    GlobalPowerRecovermentModifier = 234,
    GlobalDamageAbsorptionTargetAbility = 235,
    OverwriteVisRange = 236,
    DamageOverTimeCastDepending = 237,
    ModifyDamageIncomingAuraContingentSelfRadialAreaDamage = 238,
    SuperWeaponShadow = 239,
    NoMeleeAgainstAir = 240,
    _SuperWeaponShadowDamage = 242,
    NoCardPlay = 243,
    NoClaim = 244,
    DamageRadialAreaAmmo = 246,
    PathLayerOverride = 247,
    ChannelBlock = 248,
    Polymorph = 249,
    Delay = 250,
    ModifyDamageIncomingOnFigure = 251,
    ImmobileRoot = 252,
    GlobalModifyCorpseGather = 253,
    AbilityDependentAbility = 254,
    CorpseManager = 255,
    DisableToken = 256,
    Piercing = 258,
    ReceiveMeleeAttacks = 259,
    BuildBlock = 260,
    PreventCardPlayAuraBuilding = 262,
    GraveyardDependentRecast = 263,
    ClaimBlock = 264,
    AmmoStartup = 265,
    DamageDistribution = 266,
    SwapSquadNightGuard = 267,
    Revive = 268,
    Amok = 269,
    NoCombat = 270,
    SlowDownDisabled = 271,
    CrowdControlTimeModifier = 272,
    DamageOnMeleeHit = 273,
    IgnoreIncomingDamageModifier = 275,
    BlockRevive = 278,
    GlobalMorphState = 279,
    SpecialOnTarget = 280,
    FleshBenderBugSwitch = 281,
    TimedMorph = 282,
    GlobalBuildTimeModifier = 283,
    CardBlock = 285,
    IceShieldRegeneration = 286,
    HealOverTime = 287,
    IceShieldTimerOffset = 288,
    SpellOnVanish = 289,
    GlobalVoidAbsorption = 290,
    VoidContainer = 291,
    ConvertCorpseToHealing = 292,
    OnEntitySpawn = 293,
    OnMorph = 294,


class AbilityEffectSpecificDamageRadialArea(BaseModel):
    progress_current: float
    progress_delta: float
    damage_remaining: float

    @model_serializer
    def as_dict(self):
        return {'DamageRadialArea': self.__dict__}


class AbilityEffectSpecificDamageOverTime(BaseModel):
    tick_wait_duration: int
    ticks_left: int
    tick_damage: float

    @model_serializer
    def as_dict(self):
        return {'DamageOverTime': self.__dict__}


class AbilityEffectSpecificLinkedFire(BaseModel):
    linked: bool
    fighting: bool
    fast_cast: int
    support_cap: int
    support_production: int

    @model_serializer
    def as_dict(self):
        return {'LinkedFire': self.__dict__}


class AbilityEffectSpecificOther(BaseModel):
    """
     If you think something interesting got hidden by Other report it
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'Other': self.__dict__}


AbilityEffectSpecific = \
    (AbilityEffectSpecificDamageRadialArea |
     AbilityEffectSpecificDamageOverTime |
     AbilityEffectSpecificLinkedFire |
     AbilityEffectSpecificOther)


class AbilityEffect(BaseModel):
    id: AbilityId
    line: AbilityLine
    source: EntityId
    source_team: int
    start_tick: int
    """
     Can be zero, if not provided
    """
    end_tick: int
    """
     Can be zero, if not provided
    """
    specific: AbilityEffectSpecific


class AspectPowerProduction(BaseModel):
    """
     Used by *mostly* power wells
    """
    current_power: float
    """
     How much more power it will produce
    """
    power_capacity: float
    """
     Same as `current_power`, before it is build for the first time.
    """

    @model_serializer
    def as_dict(self):
        return {'PowerProduction': self.__dict__}


class AspectHealth(BaseModel):
    """
     Health of an entity.
    """
    current_hp: float
    """
     Actual HP that it can lose before dying.
    """
    cap_current_max: float
    """
     Current maximum including bufs and debufs.
    """

    @model_serializer
    def as_dict(self):
        return {'Health': self.__dict__}


class AspectCombat(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Combat': self.__dict__}


class AspectModeChange(BaseModel):
    current_mode: ModeId
    all_modes: List[ModeId]

    @model_serializer
    def as_dict(self):
        return {'ModeChange': self.__dict__}


class AspectAmmunition(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Ammunition': self.__dict__}


class AspectSuperWeaponShadow(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'SuperWeaponShadow': self.__dict__}


class AspectWormMovement(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'WormMovement': self.__dict__}


class AspectNPCTag(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'NPCTag': self.__dict__}


class AspectPlayerKit(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'PlayerKit': self.__dict__}


class AspectLoot(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Loot': self.__dict__}


class AspectImmunity(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Immunity': self.__dict__}


class AspectTurret(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Turret': self.__dict__}


class AspectTunnel(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Tunnel': self.__dict__}


class AspectMountBarrier(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'MountBarrier': self.__dict__}


class AspectSpellMemory(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'SpellMemory': self.__dict__}


class AspectPortal(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Portal': self.__dict__}


class AspectHate(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Hate': self.__dict__}


class AspectBarrierGate(BaseModel):
    open: bool

    @model_serializer
    def as_dict(self):
        return {'BarrierGate': self.__dict__}


class AspectAttackable(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Attackable': self.__dict__}


class AspectSquadRefill(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'SquadRefill': self.__dict__}


class AspectPortalExit(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'PortalExit': self.__dict__}


class AspectConstructionData(BaseModel):
    """
     When building / barrier is under construction it has this aspect.
    """
    refresh_count_remaining: int
    """
     Build ticks until finished.
    """
    refresh_count_total: int
    """
     Build ticks needed from start of construction to finish it.
    """
    health_per_build_update_trigger: float
    """
     How much health is added on build tick.
    """
    remaining_health_to_add: float
    """
     How much health is still missing.
    """

    @model_serializer
    def as_dict(self):
        return {'ConstructionData': self.__dict__}


class AspectSuperWeaponShadowBomb(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'SuperWeaponShadowBomb': self.__dict__}


class AspectRepairBarrierSet(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'RepairBarrierSet': self.__dict__}


class AspectConstructionRepair(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'ConstructionRepair': self.__dict__}


class AspectFollower(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Follower': self.__dict__}


class AspectCollisionBase(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'CollisionBase': self.__dict__}


class AspectEditorUniqueID(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'EditorUniqueID': self.__dict__}


class AspectRoam(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Roam': self.__dict__}


Aspect = \
    (AspectPowerProduction |
     AspectHealth |
     AspectCombat |
     AspectModeChange |
     AspectAmmunition |
     AspectSuperWeaponShadow |
     AspectWormMovement |
     AspectNPCTag |
     AspectPlayerKit |
     AspectLoot |
     AspectImmunity |
     AspectTurret |
     AspectTunnel |
     AspectMountBarrier |
     AspectSpellMemory |
     AspectPortal |
     AspectHate |
     AspectBarrierGate |
     AspectAttackable |
     AspectSquadRefill |
     AspectPortalExit |
     AspectConstructionData |
     AspectSuperWeaponShadowBomb |
     AspectRepairBarrierSet |
     AspectConstructionRepair |
     AspectFollower |
     AspectCollisionBase |
     AspectEditorUniqueID |
     AspectRoam)


class Job(IntEnum):
    NoJob = 0,
    Idle = 1,
    GoTo = 2,
    """
     also can be `GotoWormMovement`
    """
    HitTargetMelee3 = 3,
    Cast = 4,
    CastResolve = 5,
    Die = 6,
    CorpseRot = 7,
    Talk = 8,
    Freeze = 9,
    Cheer = 10,
    HitTargetMelee11 = 11,
    InstantCast = 12,
    Spawn = 13,
    Deploy = 14,
    _UnknownReportIt15 = 15,
    _UnknownReportIt16 = 16,
    _UnknownReportIt17 = 17,
    _UnknownReportIt18 = 18,
    AttackSquadWorker = 19,
    PushBackFly = 20,
    PushBackStandUp = 21,
    StampedeStart = 22,
    StampedeRun = 23,
    StampedeStop = 24,
    StampedeSquad = 25,
    BarrierCrush = 26,
    BarrierGateToggle = 27,
    FlameThrowerInit = 28,
    FlameThrowerWork = 29,
    FlameThrowerShutDown = 30,
    Nothing = 31,
    _UnknownReportIt32 = 32,
    _UnknownReportIt33 = 33,
    _UnknownReportIt34 = 34,
    Construct = 35,
    Crush = 36,
    MountBarrierSquad = 37,
    ModeChange = 38,
    TurretAim = 39,
    ChannelStart = 40,
    ChannelLoop = 41,
    ChannelEnd = 42,
    GotoWormMovement = 43,
    Morph = 44,
    _UnknownReportIt45OrMore = 255,


class Orbs(BaseModel):
    """
     Simplified version of how many monuments of each color player have
    """
    shadow: int
    nature: int
    frost: int
    fire: int
    starting: int
    """
     Can be used instead of any color, and then changes to color of first token on the used card.
    """
    white: int
    """
     Can be used only for colorless tokens on the card. (Curse Orb changes colored orb to white one)
    """
    all: int
    """
     Can be used as any color. Only provided by map scripts.
    """


class APIPlayerEntity(BaseModel):
    """
     Technically it is specific case of `APIEntity`, but we decided to move players out,
     and move few fields up like position and owning player id
    """
    id: EntityId
    """
     Unique id of the entity
    """
    effects: List[AbilityEffect]
    """
     List of effects the entity have.
    """
    aspects: List[dict] | List[Aspect]
    """
     List of aspects entity have.
    """
    team: int
    power: float
    void_power: float
    population_count: int
    name: str
    orbs: Orbs

    # noinspection PyMethodParameters
    @field_validator("aspects")
    def validate_aspects(cls, la: List[Aspect]) -> List[Aspect]:
        res = []
        for v in la:
            res.append(get_class_by_name(f"Aspect{list(v.keys())[0]}")(**v[list(v.keys())[0]]))
        return res


class MatchPlayer(BaseModel):
    name: str
    """
     Name of player.
    """
    deck: DeckAPI
    """
     Deck used by that player.
     TODO Due to technical difficulties might be empty.
    """
    entity: APIPlayerEntity
    """
     entity controlled by this player
    """


class Position(BaseModel):
    """
     `x` and `z` are coordinates on the 2D map.
    """
    x: float
    y: float
    """
     Also known as height.
    """
    z: float


class Position2D(BaseModel):
    x: float
    y: float


class OrbColor(IntEnum):
    """
     Color of an orb.
    """
    White = 0,
    Shadow = 1,
    Nature = 2,
    Frost = 3,
    Fire = 4,
    Starting = 5,
    All = 7,


class CreateOrbColor(IntEnum):
    """
     Subset of `OrbColor`, because creating the other colors does not make sense.
    """
    Shadow = 1,
    Nature = 2,
    Frost = 3,
    Fire = 4,


class APIEntitySpecificProjectile(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Projectile': self.__dict__}


class APIEntitySpecificPowerSlot(BaseModel):
    res_id: int
    state: int
    team: int

    @model_serializer
    def as_dict(self):
        return {'PowerSlot': self.__dict__}


class APIEntitySpecificTokenSlot(BaseModel):
    color: OrbColor

    @model_serializer
    def as_dict(self):
        return {'TokenSlot': self.__dict__}


class APIEntitySpecificAbilityWorldObject(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'AbilityWorldObject': self.__dict__}


class APIEntitySpecificSquad(BaseModel):
    card_id: CardId
    res_squad_id: SquadId
    bound_power: float
    squad_size: int
    figures: List[EntityId]
    """
     IDs of the figures in the squad
    """

    @model_serializer
    def as_dict(self):
        return {'Squad': self.__dict__}


class APIEntitySpecificFigure(BaseModel):
    squad_id: EntityId
    current_speed: float
    rotation_speed: float
    unit_size: int
    move_mode: int

    @model_serializer
    def as_dict(self):
        return {'Figure': self.__dict__}


class APIEntitySpecificBuilding(BaseModel):
    building_id: BuildingId
    card_id: CardId
    power_cost: float

    @model_serializer
    def as_dict(self):
        return {'Building': self.__dict__}


class APIEntitySpecificBarrierSet(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'BarrierSet': self.__dict__}


class APIEntitySpecificBarrierModule(BaseModel):
    team: int
    set: EntityId
    state: int
    slots: int
    free_slots: int
    walkable: bool

    @model_serializer
    def as_dict(self):
        return {'BarrierModule': self.__dict__}


APIEntitySpecific = \
    (APIEntitySpecificProjectile |
     APIEntitySpecificPowerSlot |
     APIEntitySpecificTokenSlot |
     APIEntitySpecificAbilityWorldObject |
     APIEntitySpecificSquad |
     APIEntitySpecificFigure |
     APIEntitySpecificBuilding |
     APIEntitySpecificBarrierSet |
     APIEntitySpecificBarrierModule)
"""
 Describes the specific types of entities
"""


class SingleTargetSingleEntity(BaseModel):
    """
     Target entity
    """
    id: EntityId

    @model_serializer
    def as_dict(self):
        return {'SingleEntity': self.__dict__}


class SingleTargetLocation(BaseModel):
    """
     Target location on the ground
    """
    xy: Position2D

    @model_serializer
    def as_dict(self):
        return {'Location': self.__dict__}


SingleTarget = \
    (SingleTargetSingleEntity |
     SingleTargetLocation)
"""
 When targeting you can target either entity, or ground coordinates.
"""


class WalkMode(IntEnum):
    PartialForce = 1,
    Force = 2,
    Normal = 4,
    """
     Also called by players "Attack move", or "Q move"
    """
    Crusade = 5,
    Scout = 6,
    Patrol = 7,


class Ping(IntEnum):
    Attention = 0,
    Attack = 1,
    Defend = 2,
    NeedHelp = 4,
    Meet = 5,


class APIEntity(BaseModel):
    """
     Entity on the map
    """
    id: EntityId
    """
     Unique id of the entity
    """
    effects: List[AbilityEffect]
    """
     List of effects the entity have.
    """
    aspects: List[dict] | List[Aspect]
    """
     List of aspects entity have.
    """
    job: Job
    """
     What is the entity doing right now
    """
    position: Position
    """
     position on the map
    """
    player_entity_id: Optional[EntityId] = None
    """
     id of player that owns this entity
    """
    specific: Dict[str, dict] | APIEntitySpecific
    """
     Player is different entity from Squad, so this is the specific part.
    """

    # noinspection PyMethodParameters
    @field_validator("aspects")
    def validate_aspects(cls, la: List[Aspect]) -> List[Aspect]:
        res = []
        for v in la:
            res.append(get_class_by_name(f"Aspect{list(v.keys())[0]}")(**v[list(v.keys())[0]]))
        return res

    # noinspection PyMethodParameters
    @field_validator("specific")
    def validate_specific(cls, v: APIEntitySpecific) -> APIEntitySpecific:
        return get_class_by_name(f"APIEntitySpecific{list(v.keys())[0]}")(**v[list(v.keys())[0]])


class APICommandBuildHouse(BaseModel):
    """
     Play card of building type.
    """
    card_position: int
    """
     TODO will be 0 when received as command by another player
    """
    xy: Position2D
    angle: float

    @model_serializer
    def as_dict(self):
        return {'BuildHouse': self.__dict__}


class APICommandCastSpellGod(BaseModel):
    """
     Play card of Spell type. (single target)
    """
    card_position: int
    target: SingleTarget

    @model_serializer
    def as_dict(self):
        return {'CastSpellGod': self.__dict__}


class APICommandCastSpellGodMulti(BaseModel):
    """
     Play card of Spell type. (line target)
    """
    card_position: int
    xy1: Position2D
    xy2: Position2D

    @model_serializer
    def as_dict(self):
        return {'CastSpellGodMulti': self.__dict__}


class APICommandProduceSquad(BaseModel):
    """
     Play card of squad type (on ground)
    """
    card_position: int
    xy: Position2D

    @model_serializer
    def as_dict(self):
        return {'ProduceSquad': self.__dict__}


class APICommandProduceSquadOnBarrier(BaseModel):
    """
     Play card of squad type (on barrier)
    """
    card_position: int
    xy: Position2D
    """
     Squad will spawn based on this position and go to the barrier.
    """
    barrier_to_mount: EntityId
    """
     Squad will go to this barrier, after spawning.
    """

    @model_serializer
    def as_dict(self):
        return {'ProduceSquadOnBarrier': self.__dict__}


class APICommandCastSpellEntity(BaseModel):
    """
     Activates spell or ability on entity.
    """
    entity: EntityId
    spell: SpellId
    target: SingleTarget

    @model_serializer
    def as_dict(self):
        return {'CastSpellEntity': self.__dict__}


class APICommandBarrierGateToggle(BaseModel):
    """
     Opens or closes gate.
    """
    barrier_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'BarrierGateToggle': self.__dict__}


class APICommandBarrierBuild(BaseModel):
    """
     Build barrier. (same as BarrierRepair if not inverted)
    """
    barrier_id: EntityId
    inverted_direction: bool

    @model_serializer
    def as_dict(self):
        return {'BarrierBuild': self.__dict__}


class APICommandBarrierRepair(BaseModel):
    """
     Repair barrier.
    """
    barrier_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'BarrierRepair': self.__dict__}


class APICommandBarrierCancelRepair(BaseModel):
    barrier_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'BarrierCancelRepair': self.__dict__}


class APICommandRepairBuilding(BaseModel):
    building_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'RepairBuilding': self.__dict__}


class APICommandCancelRepairBuilding(BaseModel):
    building_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'CancelRepairBuilding': self.__dict__}


class APICommandGroupAttack(BaseModel):
    squads: List[EntityId]
    target_entity_id: EntityId
    force_attack: bool

    @model_serializer
    def as_dict(self):
        return {'GroupAttack': self.__dict__}


class APICommandGroupEnterWall(BaseModel):
    squads: List[EntityId]
    barrier_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'GroupEnterWall': self.__dict__}


class APICommandGroupExitWall(BaseModel):
    squads: List[EntityId]
    barrier_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'GroupExitWall': self.__dict__}


class APICommandGroupGoto(BaseModel):
    squads: List[EntityId]
    positions: List[Position2D]
    walk_mode: WalkMode
    orientation: float

    @model_serializer
    def as_dict(self):
        return {'GroupGoto': self.__dict__}


class APICommandGroupHoldPosition(BaseModel):
    squads: List[EntityId]

    @model_serializer
    def as_dict(self):
        return {'GroupHoldPosition': self.__dict__}


class APICommandGroupStopJob(BaseModel):
    squads: List[EntityId]

    @model_serializer
    def as_dict(self):
        return {'GroupStopJob': self.__dict__}


class APICommandModeChange(BaseModel):
    entity_id: EntityId
    new_mode_id: ModeId

    @model_serializer
    def as_dict(self):
        return {'ModeChange': self.__dict__}


class APICommandPowerSlotBuild(BaseModel):
    slot_id: EntityId

    @model_serializer
    def as_dict(self):
        return {'PowerSlotBuild': self.__dict__}


class APICommandTokenSlotBuild(BaseModel):
    slot_id: EntityId
    color: CreateOrbColor

    @model_serializer
    def as_dict(self):
        return {'TokenSlotBuild': self.__dict__}


class APICommandPing(BaseModel):
    xy: Position2D
    ping: Ping

    @model_serializer
    def as_dict(self):
        return {'Ping': self.__dict__}


class APICommandSurrender(BaseModel):
    pass

    @model_serializer
    def as_dict(self):
        return {'Surrender': self.__dict__}


class APICommandWhisperToMaster(BaseModel):
    text: str

    @model_serializer
    def as_dict(self):
        return {'WhisperToMaster': self.__dict__}


APICommand = \
    (APICommandBuildHouse |
     APICommandCastSpellGod |
     APICommandCastSpellGodMulti |
     APICommandProduceSquad |
     APICommandProduceSquadOnBarrier |
     APICommandCastSpellEntity |
     APICommandBarrierGateToggle |
     APICommandBarrierBuild |
     APICommandBarrierRepair |
     APICommandBarrierCancelRepair |
     APICommandRepairBuilding |
     APICommandCancelRepairBuilding |
     APICommandGroupAttack |
     APICommandGroupEnterWall |
     APICommandGroupExitWall |
     APICommandGroupGoto |
     APICommandGroupHoldPosition |
     APICommandGroupStopJob |
     APICommandModeChange |
     APICommandPowerSlotBuild |
     APICommandTokenSlotBuild |
     APICommandPing |
     APICommandSurrender |
     APICommandWhisperToMaster)
"""
 All the different command bot can issue.
"""


class PlayerCommand(BaseModel):
    """
     Command that happen.
    """
    player: EntityId
    command: Dict[str, dict] | APICommand

    # noinspection PyMethodParameters
    @field_validator("command")
    def validate_command(cls, v: APICommand) -> APICommand:
        return get_class_by_name(f"APICommand{list(v.keys())[0]}")(**v[list(v.keys())[0]])


class CommandRejectionReasonOther(BaseModel):
    """
     Rejection reason for `BuildHouse`, `ProduceSquad`, and `ProduceSquadOnBarrier`
     `numbers2` mostly contains card conditions IDs that caused rejection, but sometimes it is in others
    """
    numbers1: List[int]
    numbers2: List[int]
    numbers3: List[int]

    @model_serializer
    def as_dict(self):
        return {'Other': self.__dict__}


class CommandRejectionReasonNotEnoughPower(BaseModel):
    """
     Player did not have enough power to play the card or activate the ability
    """
    player_power: float
    required: int

    @model_serializer
    def as_dict(self):
        return {'NotEnoughPower': self.__dict__}


class CommandRejectionReasonSpellDoesNotExist(BaseModel):
    """
     Player did not have enough power to play the card or activate the ability
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'SpellDoesNotExist': self.__dict__}


class CommandRejectionReasonEntityDoesNotExist(BaseModel):
    """
     The entity is not on the map
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'EntityDoesNotExist': self.__dict__}


class CommandRejectionReasonInvalidEntityType(BaseModel):
    """
     Entity exist, but type is not correct
    """
    entity_type: int

    @model_serializer
    def as_dict(self):
        return {'InvalidEntityType': self.__dict__}


class CommandRejectionReasonCanNotCast(BaseModel):
    """
     Rejection reason for `CastSpellEntity`
    """
    failed_conditions: List[int]

    @model_serializer
    def as_dict(self):
        return {'CanNotCast': self.__dict__}


class CommandRejectionReasonEntityNotOwned(BaseModel):
    """
     Bot issued command for entity it does not own
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'EntityNotOwned': self.__dict__}


class CommandRejectionReasonEntityOwnedBySomeoneElse(BaseModel):
    """
     Bot issued command for entity owned by someone else
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'EntityOwnedBySomeoneElse': self.__dict__}


class CommandRejectionReasonNoModeChange(BaseModel):
    """
     Bot issued command for entity to change mode, but the entity does not have `ModeChange` aspect.
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'NoModeChange': self.__dict__}


class CommandRejectionReasonEntityAlreadyInThisMode(BaseModel):
    """
     Trying to change to mode, in which the entity already is.
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'EntityAlreadyInThisMode': self.__dict__}


class CommandRejectionReasonModeNotExist(BaseModel):
    """
     Trying to change to moe, that the entity does not have.
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'ModeNotExist': self.__dict__}


class CommandRejectionReasonInvalidCardIndex(BaseModel):
    """
     Card index must be 0-19
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'InvalidCardIndex': self.__dict__}


class CommandRejectionReasonInvalidCard(BaseModel):
    """
     Card on the given index is invalid
    """
    pass

    @model_serializer
    def as_dict(self):
        return {'InvalidCard': self.__dict__}


CommandRejectionReason = \
    (CommandRejectionReasonOther |
     CommandRejectionReasonNotEnoughPower |
     CommandRejectionReasonSpellDoesNotExist |
     CommandRejectionReasonEntityDoesNotExist |
     CommandRejectionReasonInvalidEntityType |
     CommandRejectionReasonCanNotCast |
     CommandRejectionReasonEntityNotOwned |
     CommandRejectionReasonEntityOwnedBySomeoneElse |
     CommandRejectionReasonNoModeChange |
     CommandRejectionReasonEntityAlreadyInThisMode |
     CommandRejectionReasonModeNotExist |
     CommandRejectionReasonInvalidCardIndex |
     CommandRejectionReasonInvalidCard)
"""
 Reason why command was rejected
"""


class RejectedCommand(BaseModel):
    """
     Command that was rejected.
    """
    player: EntityId
    reason: Dict[str, dict] | CommandRejectionReason
    command: Dict[str, dict] | APICommand

    # noinspection PyMethodParameters
    @field_validator("reason")
    def validate_reason(cls, v: CommandRejectionReason) -> CommandRejectionReason:
        return get_class_by_name(f"CommandRejectionReason{list(v.keys())[0]}")(**v[list(v.keys())[0]])

    # noinspection PyMethodParameters
    @field_validator("command")
    def validate_command(cls, v: APICommand) -> APICommand:
        return get_class_by_name(f"APICommand{list(v.keys())[0]}")(**v[list(v.keys())[0]])


class AiForMapAPI(BaseModel):
    """
     Response on the `/hello` endpoint.
    """
    name: str
    """
     The unique name of the bot.
    """
    decks: List[DeckAPI]
    """
     List of decks this bot can use on the map.
     Empty to signalize, that bot can not play on given map.
    """


class APIGameStartState(BaseModel):
    """
     Used in `/start` endpoint.
    """
    your_player_id: EntityId
    """
     Tells the bot which player it is supposed to control.
    """
    players: List[MatchPlayer]
    """
     Players in the match.
    """
    entities: List[APIEntity]
    """
     All the relevant entities on the map. (For example it does not list all the rocks and trees)
    """


class APIGameState(BaseModel):
    """
     Used in `/tick` endpoint, on every tick from 2 forward.
    """
    current_tick: int
    """
     Time since start of the match measured in ticks.
     One tick is 0.1 second = 100 milliseconds = (10 ticks per second)
     Each tick is 100 ms. 1 second is 10 ticks. 1 minute is 600 ticks.
    """
    commands: List[PlayerCommand]
    """
     Commands that will be executed this tick.
    """
    rejected_commands: List[RejectedCommand]
    """
     Commands that was rejected.
    """
    players: List[APIPlayerEntity]
    """
     player entities in the match
    """
    entities: List[APIEntity]
    """
     All the relevant entities on the map. (For example it does not list all the rocks and trees)
    """


class APIPrepare(BaseModel):
    """
     Used in `/prepare` endpoint
    """
    deck: str
    """
     Name of deck, selected from `AiForMapAPI` returned by `/hello` endpoint.
    """
    map_info: MapInfo
    """
     Repeating `map_info` in case bot want to prepare differently based on map.
    """


class ApiHello(BaseModel):
    """
     Used in `/hello` endpoint
    """
    version: int
    """
     Must match the version in this file, to guarantee structures matching.
    """
    map: MapInfo
    """
     Myp about which is the game asking.
    """


