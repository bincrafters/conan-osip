#include <cstdlib>

#include "osipparser2/osip_message.h"

int main() {
    osip_message_t *sip = NULL;

    if (osip_message_init(&sip) != 0) {
        fprintf(stderr, "Could not initialize oSIP properly.\n");
        return EXIT_FAILURE;
    }
    osip_message_free(sip);

    return EXIT_SUCCESS;
}
