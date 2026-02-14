PORTNAME=	chankro
DISTVERSION=	21.7b6e844
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool that generates a PHP capable of run a custom binary (like a meterpreter) or a bash script (p.e. reverse shell) bypassing disable_functions & open_basedir).
WWW=		https://github.com/TarlogicSecurity/Chankro

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
