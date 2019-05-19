$(document).ready(function () {

    const gwdBosses = $('#god_wars_dungeon_bosses');
    const dagKings = $('#dagannoth_kings');
    const wildyBosses = $('#wilderness_bosses');
    const slayerBosses = $('#slayer_bosses');

    const zilyana = $('#id_zilyana');
    const graardor = $('#id_graardor');
    const kreeArra = $('#id_kree_arra');
    const kril = $('#id_kril_tsutsaroth');

    const prime = $('#id_prime');
    const rex = $('#id_rex');
    const supreme = $('#id_supreme');

    const callisto = $('#id_callisto');
    const chaosElemental = $('#id_chaos_elemental');
    const scorpia = $('#id_scorpia');
    const venenatis = $('#id_venenatis');
    const vetion = $('#id_vetion');

    const abyssalSire = $('#id_abyssal_sire');
    const cerberus = $('#id_cerberus');
    const grotesqueGuardians = $('#id_grotesque_guardians');
    const kraken = $('#id_kraken');
    const thermy = $('#id_thermonuclear_smoke_devil');

    gwdBosses.change(function () {
        var checked = gwdBosses.is(':checked');

        zilyana.prop('checked', checked);
        graardor.prop('checked', checked);
        kreeArra.prop('checked', checked);
        kril.prop('checked', checked);
    });

    dagKings.change(function() {
        var checked = dagKings.is(':checked');

        prime.prop('checked', checked);
        rex.prop('checked', checked);
        supreme.prop('checked', checked);
    });

    wildyBosses.change(function() {
        var checked = wildyBosses.is(':checked');

        callisto.prop('checked', checked);
        chaosElemental.prop('checked', checked);
        scorpia.prop('checked', checked);
        venenatis.prop('checked', checked);
        vetion.prop('checked', checked);
    });

    slayerBosses.change(function() {
        var checked = slayerBosses.is(':checked');

        abyssalSire.prop('checked', checked);
        cerberus.prop('checked', checked);
        grotesqueGuardians.prop('checked', checked);
        kraken.prop('checked', checked);
        thermy.prop('checked', checked);
    });
});

